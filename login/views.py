from django.shortcuts import HttpResponse, render, redirect
from .models import User
from django.urls import reverse
from functools import wraps

# Create your views here.

# 装饰器
# cookie
'''
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.get_signed_cookie("login", salt="hehe", default=None) == "chenqianyu":
            print("decoractor is running 1")
            # 已经登录的用户...
            return func(request, *args, **kwargs)
        else:
            # 没有登录的用户，跳转刚到登录页面
            print("decoractor is running 2")
            return redirect("/login/")
    return inner

'''


# session
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        is_login = request.session.get("login")
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/")

    return inner


# 登陆验证


# cookie
'''
def login_func(request):
    if request.method == "POST":
        username_get = request.POST.get("username").strip()
        password_get = request.POST.get("password").strip()
        user_obj = User.objects.filter(username=username_get)
        if user_obj:
            if user_obj[0].password == password_get:
                rep = redirect(reverse("sc:manage"))
                rep.set_signed_cookie("login", "chenqianyu", salt='hehe')
                return rep
            else:
                return HttpResponse("<script>alert('密码错误')</script>")
        else:
            return HttpResponse("<script>alert('用户名不存在')</script>")
    return render(request, "login/login.html")
'''

# session
'''
def login_func(request):
    if request.method == "POST":
        username_get = request.POST.get("username").strip()
        password_get = request.POST.get("password").strip()
        user_obj = User.objects.filter(username=username_get)
        if user_obj:
            if user_obj[0].password == password_get:
                rep = redirect(reverse("sc:manage"))
                request.session['login'] = True
                request.session['username'] = username_get
                return rep
            else:
                return HttpResponse("<h2>密码错误</h2>")
        else:
            return HttpResponse("<h2>用户名不存在</h2>")
    return render(request, "login/login.html")
'''


# ajax login
def login_func(request):
    if request.method == "POST":
        username_get = request.POST.get("username").strip()
        password_get = request.POST.get("password").strip()
        user_obj = User.objects.filter(username=username_get)
        if user_obj:
            print(user_obj,"--------1")
            if user_obj[0].password == password_get:
                request.session['login'] = True
                request.session['username'] = username_get
                ret = {"status": 1, "msg": "登陆成功"}
            else:
                ret = {"status": 3, "msg": "密码错误"}
        else:
            print(user_obj, "--------2")
            ret = {"status": 2, "msg": "账号错误"}
            print(ret)
        from django.http import JsonResponse
        return JsonResponse(ret)

    return render(request, "login/login.html")



#注册
def register(request):
    if request.method == "POST":
        username_get = request.POST.get("username").strip()
        password_get = request.POST.get("password").strip()
        user_obj = User.objects.filter(username=username_get)
        if user_obj:
            ret = {"status": 1, "msg": "用户名已经存在"}
        else:
            User.objects.create(username=username_get,password=password_get)
            ret = {"status": 2, "msg": "用户名注册成功"}

        from django.http import JsonResponse
        return JsonResponse(ret)

    return render(request,"login/register.html")



# 404页面
def not_found(request):
    return render(request, '404/index.html')


# 注销
# cookie
'''
def login_out(request):
    rep = redirect("/login/")
    rep.delete_cookie("login")  # 删除用户浏览器上之前设置的usercookie值
    return rep

'''


# session
def login_out(request):
    rep = redirect("/login/")
    del request.session["login"]
    return rep


# ajax测试
def ajax_add(request):
    i1 = int(request.GET.get("i1", 0))
    i2 = int(request.GET.get("i2", 0))
    ret = i1 + i2
    return HttpResponse(ret)


def add(request):
    i1 = int(request.GET.get("i1", 0))
    i2 = int(request.GET.get("i2", 0))
    ret = i1 + i2
    return render(request, "Ajax.html", {"i1": i1, "i2": i2, "ret": ret})



