from django.db import models


# Create your models here.
# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=64)
    addr = models.CharField(max_length=64)


# 书籍
class Book(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField()
    publisher = models.ForeignKey("Publisher")


# 作者
class Writer(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateField()
    books = models.ManyToManyField("Book")
