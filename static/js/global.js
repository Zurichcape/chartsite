(function (factory) {
	if (typeof define === 'function' && define.amd) {
		// AMD
		define(['jquery'], factory);
	} else if (typeof exports === 'object') {
		// CommonJS
		factory(require('jquery'));
	} else {
		// Browser globals
		factory(jQuery);
	}
}(function ($) {

    let config = $.cookie = function (key, value, options) {

        // Write

        if (value !== undefined && !$.isFunction(value)) {
            options = $.extend({}, config.defaults, options);

            if (typeof options.expires === 'number') {
                let days = options.expires, t = options.expires = new Date();
                t.setTime(+t + days * 864e+5);
            }

            return (document.cookie = [
                encode(key), '=', stringifyCookieValue(value),
                options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                options.path    ? '; path=' + options.path : '',
                options.domain  ? '; domain=' + options.domain : '',
                options.secure  ? '; secure' : ''
            ].join(''));
        }

        // Read

        let result = key ? undefined : {};

        // To prevent the for loop in the first place assign an empty array
        // in case there are no cookies at all. Also prevents odd result when
        // calling $.cookie().
        let cookies = document.cookie ? document.cookie.split('; ') : [];

        let i = 0, l = cookies.length;
        for (; i < l; i++) {
            let parts = cookies[i].split('=');
            let name = decode(parts.shift());
            let cookie = parts.join('=');

            if (key && key === name) {
                // If second argument (value) is a function it's a converter...
                result = read(cookie, value);
                break;
            }

            // Prevent storing a cookie that we couldn't decode.
            if (!key && (cookie = read(cookie)) !== undefined) {
                result[name] = cookie;
            }
        }

        return result;
    };
    let pluses = /\+/g;

    function encode(s) {
		return config.raw ? s : encodeURIComponent(s);
	}

	function decode(s) {
		return config.raw ? s : decodeURIComponent(s);
	}

	function stringifyCookieValue(value) {
		return encode(config.json ? JSON.stringify(value) : String(value));
	}

	function parseCookieValue(s) {
		if (s.indexOf('"') === 0) {
			// This is a quoted cookie as according to RFC2068, unescape...
			s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
		}

		try {
			// Replace server-side written pluses with spaces.
			// If we can't decode the cookie, ignore it, it's unusable.
			// If we can't parse the cookie, ignore it, it's unusable.
			s = decodeURIComponent(s.replace(pluses, ' '));
			return config.json ? JSON.parse(s) : s;
		} catch(e) {}
	}

	function read(s, converter) {
        let value = config.raw ? s : parseCookieValue(s);
        return $.isFunction(converter) ? converter(value) : value;
	}


    config.defaults = {};

	$.removeCookie = function (key, options) {
		if ($.cookie(key) === undefined) {
			return false;
		}

		// Must not alter options, thus extending a fresh object...
		$.cookie(key, '', $.extend({}, options, { expires: -1 }));
		return !$.cookie(key);
	};

}));

$(function () {
    if (!$.cookie('token')) {
        let user = $("#user");
        user.empty().append('<li><a href="/user/login"><i class="fa fa fa-sign-in"></i> 登录</a></li>');
        if (user.hasClass("profile")){
            user.removeClass("profile")
        }
        user.append('<li><a href="/user/register"><i class="fa fa-pencil"></i>  注册</a></li>');
    }
    else {
        $.ajax({
            url: "/users/1/",
            beforeSend: function (xhr) {
                // //发送ajax请求之前向http的head里面加入验证信息
                xhr.setRequestHeader("Authorization", "token " + $.cookie('token')); // 请求发起前在头部附加token
            },
            success: function (data, status) {
                let name;
                let userinfo = $("#userInfo");
                if (data.first_name) {
                name = data.first_name
                }
                else {name = data.email}
                $("#user").addClass("profile");
                $("#user").empty().append('<li id="userInfo" class="dropdown">' +
                    '                    <a href="/personal/" class="dropdown-toggle" >' +
                    '                        <img class="img-circle" src='+ data.image +'>' + name +
                    '                        <b class="caret"></b>' +
                    '                    <span class="fa fa-envelope pull-right message" style="font-size: 1.5em; display: none;"> <span class="navbar-unread count">100</span></span></a>' +
                    '                    <ul id="userMenu" class="dropdown-menu" style="display: none;">' +
                    '                        <li>' +
                    '                            <a href="/personal">我的消息' +
                    '                                <span class="fa fa-envelope pull-right"></span>' +
                    '                            </a>' +
                    '                        </li>' +
                    '                        <li class="divider"></li>' +
                    '                        <li><a href="/account">账号设置' +
                    '                                <span class="glyphicon glyphicon-cog pull-right"></span></a>' +
                    '                        </li>' +
                    '                        <li class="divider"></li>' +
                    '                        <li>' +
                    '                            <a href="http://i.hubwiz.com/invite">邀请朋友' +
                    '                                <span class="fa fa-users pull-right"></span>' +
                    '                            </a>' +
                    '                        </li>' +
                    '                        <li class="divider"></li>' +
                    '                        <li><a href="#" id="logout">安全退出' +
                    '                                <span class="glyphicon glyphicon-log-out pull-right"></span></a>' +
                    '                        </li>' +
                    '                    </ul>' +
                    '                </li>')
            },
        })
    }
});



$(function(){
    //刷新验证码
    $(".captcha").click(function(){
        $.get("/captcha/refresh/?"+Math.random(), function(result){
                $("#id_captcha_1").val('').focus();
                $('.captcha').attr("src",result.image_url);
                $('#id_captcha_0').attr("value",result.key);
            });
    });
    $("#logout").click(function () {
        delete document.cookie;
    });
    $("#labBtn").click(function(){location.href="/share/"});
});





