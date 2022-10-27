from django.db import models
from utils.models import BaseBannerModel


# Create your models here.
# 鉴于首页banner图有点多，难以取舍,每一个分类写一个类


class HotBanner(BaseBannerModel):
    """
    热门景点轮播图
    """
    title = models.CharField(max_length=32, help_text='标题', verbose_name='标题')
    link = models.CharField(max_length=128, help_text='链接', verbose_name='链接')
    desc = models.CharField(max_length=128, help_text='描述', verbose_name='图片美景描述')
    img = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='上传图片', help_text='图片长宽固定的')

    # 图片后期可能会使用oss存储对象

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'hahaha_hotbanner'
        verbose_name = '首页热门景点轮播图'
        verbose_name_plural = verbose_name


class Tag(BaseBannerModel):
    """
    首页分类轮播图标签
    """
    name = models.CharField(max_length=32, verbose_name='标签名', help_text='标签')

    class Meta:
        db_table = 'hahaha_tag'
        verbose_name = '首页分类轮播图标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TagBanner(BaseBannerModel):
    tag = models.ForeignKey(to='Tag', on_delete=models.SET_NULL, null=True, blank=True, db_constraint=False,
                            verbose_name='轮播图分类', help_text='轮播图分类')
    title = models.CharField(max_length=32, help_text='标题', verbose_name='标题')
    link = models.CharField(max_length=128, help_text='链接', verbose_name='链接')
    desc = models.CharField(max_length=128, help_text='描述', verbose_name='图片美景描述')
    img = models.ImageField(upload_to='banner/tag/', blank=True, null=True, verbose_name='上传图片', help_text='图片长宽固定的')

    class Meta:
        db_table = 'hahaha_tagbanner'
        verbose_name = '首页分类轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '分类轮播图' + self.title


class TopBanner(BaseBannerModel):

    """
    顶级景点轮播图
    """
    title = models.CharField(max_length=32, help_text='标题', verbose_name='标题')
    link = models.CharField(max_length=128, help_text='链接', verbose_name='链接',null=True,blank=True)
    desc = models.CharField(max_length=128, help_text='描述', verbose_name='图片美景描述')
    img = models.ImageField(upload_to='banner', blank=True, null=True, verbose_name='上传图片', help_text='图片长宽固定的')



    def __str__(self):
        return self.title

    class Meta:
        db_table = 'hahaha_topbanner'
        verbose_name = '首页顶级轮播图'
        verbose_name_plural = verbose_name
