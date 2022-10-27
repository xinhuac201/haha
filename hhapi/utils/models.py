from django.db import models


# 所有首页所有轮播图
class BaseBannerModel(models.Model):
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=False, verbose_name='是否展示')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True)
    order = models.IntegerField(verbose_name='顺序', null=True)

    class Meta:  # 不在数据库生成
        abstract = True

# class BaseModel(models.Model):
#     pass
