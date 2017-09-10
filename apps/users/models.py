from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, default='', verbose_name='姓名')
    birth = models.DateTimeField(default=datetime.now, verbose_name='生日')
    gender = models.CharField(max_length=6, default='female', choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    mobile = models.CharField(max_length=11, default='', unique=True, verbose_name='手机号')
    email = models.CharField(max_length=30, unique=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


