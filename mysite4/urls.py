"""mysite4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from school.views import manage, delete_class, edit_class, add_class, student_list, delete_student, add_student, \
#     edit_student, teacher_list, delete_teacher, add_teacher, edit_teacher
from login.views import login_func, not_found, login_out, add, ajax_add, register
from publisher.views import publisher_list, add_publisher, delete_publisher, edit_publisher, book_list, add_book, \
    delete_book, edit_book, writer_list, delete_writer, add_writer, edit_writer
from school import urls as school_urls

# from publisher import urls as publisher_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 命名分组

    # 学校  只命名了学校的  出版社的没动
    url(r"^school/", include(school_urls, namespace='sc')),

    # 登陆相关
    url(r'^login/', login_func),
    url(r'^logout/', login_out, name='logout'),
    url(r'^register/', register, name="register"),

    # 出版社相关操作
    url(r'^publisher_list/', publisher_list),
    url(r'^delete_publisher', delete_publisher),
    url(r'^add_publisher/', add_publisher),
    url(r'^edit_publisher', edit_publisher),
    # 书籍相关操作
    url(r'^book_list/', book_list),
    url(r'^add_book/', add_book),
    url(r'^delete_book', delete_book),
    url(r'^edit_book', edit_book),
    # 作者相关操作
    url(r"^writer_list/", writer_list),
    url(r'^delete_writer', delete_writer),
    url(r"^add_writer/", add_writer),
    url(r"^edit_writer", edit_writer),

    # ajax测试
    url(r"^add/", add),
    url(r"^ajax_add/", ajax_add),

    # 404
    url(r"$", not_found),
]






# 出版社
# url(r"^publisher/", include(publisher_urls, namespace='pb')),

# # 班级表相关
# url(r'^manage/', manage, name='manage'),
# url(r'^delete_class/', delete_class),
# url(r'^edit_class/', edit_class),
# url(r'^add_class/', add_class),
# # 学生表相关操作
# url(r'^student_list/', student_list),
# url(r'^delete_student/', delete_student),
# url(r'^add_student/', add_student),
# url(r'^edit_student/', edit_student),
# # 老师表相关操作
# url(r"^teacher_list/", teacher_list),
# url(r"^delete_teacher", delete_teacher),
# url(r'^add_teacher/', add_teacher),
# url(r'^edit_teacher/', edit_teacher),
