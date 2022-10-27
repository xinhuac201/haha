from django.db import models
from utils.models import BaseBannerModel


# Create your models here.


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'category'
        verbose_name = '旅游分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '旅游分类' + self.name


class Banner(BaseBannerModel):
    category = models.ForeignKey(to='Category', on_delete=models.SET_NULL, null=True, blank=True, db_constraint=False,
                                 verbose_name='轮播图分类', help_text='轮播图分类')
    title = models.CharField(max_length=32, help_text='标题', verbose_name='标题')
    link = models.CharField(max_length=128, help_text='链接', verbose_name='链接')
    desc = models.CharField(max_length=128, help_text='描述', verbose_name='图片美景描述')
    img = models.ImageField(upload_to='banner/category/', blank=True, null=True, verbose_name='上传图片',
                            help_text='图片长宽固定的')

    class Meta:
        db_table = 'banner'
        verbose_name = '旅游分类轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '旅游分类轮播图' + self.title


class Area(models.Model):
    """
    区域
    """
    name = models.CharField(max_length=64, verbose_name="区域")
    country = models.ForeignKey(to="Country", on_delete=models.DO_NOTHING, blank=True)

    class Meta:
        db_table = 'area'
        verbose_name = '旅游分类轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '旅游分类轮播图' + self.name


#
class Country(models.Model):
    """
    国家
    """
    name = models.CharField(max_length=64, verbose_name="国家")

    class Meta:
        db_table = 'country'
        verbose_name = '国家'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '旅游分类轮播图' + self.name


class Holiday(models.Model):
    """
    假期
    """
    name = models.CharField(max_length=64, verbose_name="假期名称")

    class Meta:
        db_table = 'holiday'
        verbose_name = '假期表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '假期' + self.name


class Overview(models.Model):
    """
    旅游线路地点
    """
    name = models.CharField(max_length=128, verbose_name="旅游线路地点")

    class Meta:
        db_table = 'overview'
        verbose_name = '具体路线地点图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '具体路线地点图' + self.name


class FocusTag(models.Model):
    name = models.CharField(max_length=64, verbose_name="聚合标签")

    class Meta:
        db_table = 'focus_tag'
        verbose_name = '聚合标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '聚合标签' + self.name


class Route(models.Model):
    """
    旅游线路
    """
    status_choices = (
        (0, '上线'),
        (1, '下线'),

    )
    routeId = models.BigIntegerField(verbose_name="线路编号")
    visa = models.CharField(null=True, blank=True, max_length=255, verbose_name="签证")
    heading = models.CharField(max_length=255, verbose_name="一级标题", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="二级标题")
    overview = models.ManyToManyField(to="Overview", verbose_name="线路地点",null=True)  # 一对多
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="线路状态")
    desc = models.TextField(verbose_name="描述",null=True,blank=True)
    cover = models.ImageField(upload_to='banner/cover/', blank=True, null=True, verbose_name='上传封面图片',
                              help_text='图片长宽固定的')
    map = models.ImageField(upload_to='banner/map/', blank=True, null=True, verbose_name='上传路线图片',
                            help_text='图片长宽固定的')
    destination = models.ForeignKey(to="Area", on_delete=models.SET_NULL, verbose_name="目的地",null=True)
    routeSort = models.IntegerField(verbose_name="线路排序")
    category = models.ForeignKey(to="Category", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="分类")
    duration = models.SmallIntegerField(verbose_name="周期", default=0)
    price = models.IntegerField(default=0, verbose_name="价格")
    focus_tag = models.ManyToManyField(to="FocusTag", verbose_name="聚合标签",null=True)
    strength = models.FloatField(verbose_name="体能系数", default=0)

    class Meta:
        db_table = 'route'
        verbose_name = '路线'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '旅游路线图' + self.title

    def overview_list(self):
        li = []
        for item in self.overview.all():
            li.append(item.name)
        return li

    def focus_tag_list(self):
        li = []
        for item in self.focus_tag.all():
            li.append(item.name)
        return li
