from django.conf.urls import url
from . import views as school_views

urlpatterns = [
    # 班级表相关
    url(r'^manage/', school_views.manage, name='manage'),
    url(r'^delete_class/', school_views.delete_class, name="delete_class"),
    url(r'^edit_class/', school_views.edit_class, name="edit_class"),
    url(r'^add_class/', school_views.add_class, name="add_class"),
    # 学生表相关操作
    url(r'^student_list/', school_views.student_list, name='student_list'),
    url(r'^delete_student/', school_views.delete_student, name='delete_student'),
    url(r'^add_student/', school_views.add_student, name="add_student"),
    url(r'^edit_student/', school_views.edit_student, name="edit_student"),
    # 老师表相关操作
    url(r"^teacher_list/", school_views.teacher_list, name='teacher_list'),
    url(r"^delete_teacher", school_views.delete_teacher, name="delete_teacher"),
    url(r'^add_teacher/', school_views.add_teacher, name="add_teacher"),
    url(r'^edit_teacher/', school_views.edit_teacher, name="edit_teacher"),
]
