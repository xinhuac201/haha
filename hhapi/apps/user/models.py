from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号码')
    # 需要pillow包的支持
    icon = models.ImageField(upload_to='icon', default='icon/default.png', verbose_name='头像')

    class Meta:
        db_table = 'hahaha_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
