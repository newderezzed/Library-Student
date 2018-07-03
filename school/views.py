from django.shortcuts import HttpResponse, render, redirect
from .models import Classes, Student, Teacher
from django.urls import reverse
from login.views import check_login

# Create your views here.


# 班级的操作 start
@check_login
def manage(request):
    print("进来了。。。", request.GET)
    data = Classes.objects.all()
    data_num = data.count()
    current_page = request.GET.get("page",1)
    from utils import mypage
    obj = mypage.Pagenation(data_num,current_page,"/school/manage/")
    class_list = data[obj.start:obj.end]
    page_html = obj.page_html()

    return render(request,
                  "school/class_list.html",
                  {"class_list": class_list,"page_html":page_html})
'''
def manage(request):
    print("进来了。。。", request.GET)
    data = Classes.objects.all()
    data_num = data.count()
    current_page = request.GET.get("page",1)
    from utils import mypage
    obj = mypage.Pagenation(data_num,current_page,"/school/manage/")
    class_list = data[obj.start:obj.end]
    page_html = obj.page_html()

    return render(request,
                  "school/class_list.html",
                  {"class_list": class_list,"page_html":page_html})
'''
# @check_login
# def delete_class(request):
#     print('----------', request.GET)
#     # 获取到那边啊标签传递过来的id
#     delete_id = request.GET.get("id")
#     # 根据id去数据库取到对应的数据
#     class_obj = Classes.objects.get(id=delete_id)
#     # 删除
#     class_obj.delete()
#
#     return redirect(reverse("sc:manage"))


@check_login
def delete_class(request):
    if request.method == 'POST':
        delete_id = request.POST.get("id")
        print(delete_id)
        Classes.objects.filter(id=delete_id).delete()
        data = {'status':1}
        # from django.http import JsonResponse
        # return JsonResponse(data)
        return HttpResponse(1)


@check_login
def edit_class(request):
    # 把要编辑的班级的ID获取到
    edit_class_id = request.GET.get("id")  # 可以取到url里面的参数
    print("--------", request.GET)
    # 根据id找到对应的班级
    class_obj = Classes.objects.get(id=edit_class_id)
    if request.method == "POST":
        # 表示用户修改好了 把数据给我发过来了
        new_class_name = request.POST.get("class_name")  # 通过表单的name属性获取

        print('=========', request.POST)
        # 更新班级名称
        class_obj.name = new_class_name
        # 保存到数据库
        class_obj.save()
        # 跳转 看是否修改成功
        return redirect(reverse("sc:manage"))
    class_name = class_obj.name
    return render(request, "school/edit_class.html", {"class": class_obj})

@check_login
def add_class(request):
    if request.method == 'POST':
        new_class_name = request.POST.get("class_name")
        print('===========', request.POST)
        new_obj = Classes.objects.create(name=new_class_name)
        return redirect(reverse("sc:manage"))

    return render(request, "school/add_class.html")


# 班级的操作 end


# 学生的操作 start
@check_login
def student_list(request):
    data = Student.objects.all()
    return render(request, "school/student_list.html", {"student_list": data, })

@check_login
def delete_student(request):
    delete_id = request.GET.get("id")

    student_obj = Student.objects.get(id=delete_id)

    student_obj.delete()

    return redirect(reverse("sc:student_list"))

@check_login
def add_student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")
        Student.objects.create(name=student_name, classes_id=class_id)
        return redirect(reverse("sc:student_list"))
    data = Classes.objects.all()
    return render(request, "school/add_student.html", {"class_list": data})

@check_login
def edit_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")

        obj = Student.objects.get(id=student_id)
        obj.name = student_name
        obj.classes_id = class_id
        obj.save()

        return redirect(reverse("sc:student_list"))

    edit_id = request.GET.get("id")
    obj = Student.objects.get(id=edit_id)
    data = Classes.objects.all()
    return render(request, "school/edit_student.html", {"student": obj, "class_list": data})


# 学生的操作 end

# 老师的操作 start
@check_login
def teacher_list(request):
    data = Teacher.objects.all()
    return render(request, "school/teacher_list.html", {"teacher_list": data, })

@check_login
def delete_teacher(request):
    delete_id = request.GET.get("id")
    Teacher.objects.get(id=delete_id).delete()

    return redirect(reverse("sc:teacher_list"))

@check_login
def add_teacher(request):
    if request.method == "POST":
        teacher_name = request.POST.get("teacher_name")
        class_ids = request.POST.getlist('class_id')

        teacher_obj = Teacher.objects.create(name=teacher_name)
        teacher_obj.classes.set(class_ids)
        teacher_obj.save()
        return redirect(reverse("sc:teacher_list"))

    class_list = Classes.objects.all()
    return render(request, "school/add_teacher.html", {"class_list": class_list})

@check_login
def edit_teacher(request):
    if request.method == "POST":
        edit_id = request.POST.get("teacher_id")
        teacher_name = request.POST.get("teacher_name")
        class_ids = request.POST.getlist("class_id")

        teacher_obj = Teacher.objects.get(id=edit_id)
        teacher_obj.name = teacher_name
        teacher_obj.classes.set(class_ids)
        teacher_obj.save()

        return redirect(reverse("sc:teacher_list"))

    edit_id = request.GET.get("id")
    teacher_obj = Teacher.objects.get(id=edit_id)
    class_list = Classes.objects.all()

    return render(request, "school/edit_teacher.html", {"teacher": teacher_obj, "class_list": class_list})

# 老师的操作 end
