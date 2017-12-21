import os

from captcha.models import CaptchaStore
from django.contrib.auth import get_user_model, authenticate, login
from random import choice
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from chartsite.settings import YUN_KEY
from apps.users.models import PhoneCode, EmailCode, ImageCode, UserProfile
from operation.models import UserMessage
from users.forms import RegisterForm, LoginForm, CaptchaForm
from users.serializers import PhoneSerialier, UserRegSerializer, UserDetailSerializer, EmailSerialier, \
    ImageCodeSerialier, ImageCodeVerifySerialier

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import authentication

from utils.code import SmsEmailCode, ImgEmailCode
from utils.code import SmsPhoneCode
from rest_framework.mixins import CreateModelMixin


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.code import send_email
User = get_user_model()


class CustomBBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class PhoneCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送手机验证码
    """
    serializer_class = PhoneSerialier

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        code = self.generate_code()

        mobile = serializer.validated_data['mobile']

        yun_pian = SmsPhoneCode(YUN_KEY)

        sms_status = yun_pian.send_msg(code=code, mobile=mobile)
        if sms_status['code'] != 0:
            return Response({
                "mobile": sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = PhoneCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED)


class EmailCodeViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮箱验证码
    """
    serializer_class = EmailSerialier

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        code = self.generate_code()

        email = serializer.validated_data['email']
        send_type = serializer.validated_data['send_type']

        sms_status = send_email(code=code, email=email, send_type=send_type)

        if not sms_status['code']:
            return Response({
                "status": sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = EmailCode(code=code, email=email)
            code_record.save()
            return Response({
                'status': sms_status['msg']
            }, status=status.HTTP_201_CREATED)


class ImageCodeViewset(mixins.ListModelMixin,  mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送图片验证码
    """
    serializer_class = ImageCodeSerialier

    def get_queryset(self):
        code = self.generate_code()
        Image = ImgEmailCode(code=code)
        img_path, image = Image.made_code_img()
        image = os.path.join('chartsite', 'captcha', image)
        ImageCode.objects.create(code=code, image=image)
        with open(img_path, 'rb') as f:
            ret = f.read()
        return ret

    def list(self, request, *args, **kwargs):
        parses = request.query_params
        header = {
            "status": status.HTTP_200_OK,
            'content_type': "text/plain"
        }
        if parses:
            parses = dict(parses)
            result = ImageCode.objects.get(code=dict(parses.keys())[0]).exists()
            if result:
                data = "OK"
            else:
                data = "Not Found"
                header['status'] = status.HTTP_404_NOT_FOUND
        else:
            data = self.get_queryset()
            header['content_type'] = "image/png"
        return HttpResponse(content=data, **header)

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)


class ImageCodeVerifyViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    验证图片验证码
    """
    serializer_class = ImageCodeVerifySerialier

    def list(self, request, *args, **kwargs):
        # data = dict(request.GET)
        # print(data)
        data = {
            'verify': request.GET['verify'],
            'captcha_0': request.GET['captcha_0'],
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)  # drf可以捕做捉异常返回400
        response = serializer.validated_data['response']
        hashkey = serializer.validated_data['hashkey']

        result = CaptchaStore.objects.filter(response=str(response).lower(), hashkey=hashkey)
        header = {
            "status": status.HTTP_200_OK,
            'content_type': "text/plain"
        }
        if result:
            data = "OK"
        else:
            data = "Not Found"
            header['status'] = status.HTTP_404_NOT_FOUND
        return HttpResponse(content=data, **header)


class UserViewset(CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    # serializer_class = UserRegSerializer
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated(), ]
        elif self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer

        return UserDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # 重载获取用户model的实例
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "user/register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "user/register.html", {"register_form": register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册农业统计数据可视化平台"
            user_message.save()

            send_email(user_name, "register")
            return render(request, "user/login.html")
        else:
            return render(request, "user/register.html", {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        login_form = RegisterForm()
        return render(request, "user/login.html", {'register_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "user/login.html", {"msg": "用户未激活！"})
            else:
                return render(request, "user/login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "user/login.html", {"login_form": login_form})


class PersonalViewset(View):
    def get(self, request):
        return render(request, "user/personal.html")


class ForgetView(View):
    def get(self, request):
        return render(request, "user/forgetpwd.html")


class AccountView(View):
    def get(self, request):
        return render(request, "user/account.html")


class ServiceView(View):
    def get(self, request):
        return render(request, "service.html")