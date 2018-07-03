from django.db import models


# Create your models here.
# 班级表
class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64, default='沙河赋腾国际')

    def __str__(self):
        return self.name


# 学生表
class Student(models.Model):
    name = models.CharField(max_length=32)
    classes = models.ForeignKey("Classes")

    def __str__(self):
        return self.name


# 老师表
class Teacher(models.Model):
    name = models.CharField(max_length=32)
    classes = models.ManyToManyField("classes")

    def __str__(self):
        return self.name
