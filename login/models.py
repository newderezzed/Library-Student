from django.db import models

# Create your models here.
# 定义一个用户
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
