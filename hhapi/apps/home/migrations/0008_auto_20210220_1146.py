# Generated by Django 2.2.2 on 2021-02-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('order', models.IntegerField(null=True, verbose_name='顺序')),
                ('title', models.CharField(help_text='标题', max_length=32, verbose_name='标题')),
                ('link', models.CharField(help_text='链接', max_length=128, verbose_name='链接')),
                ('desc', models.CharField(help_text='描述', max_length=128, verbose_name='图片美景描述')),
                ('img', models.ImageField(blank=True, help_text='图片长宽固定的', null=True, upload_to='banner', verbose_name='上传图片')),
            ],
            options={
                'verbose_name': '首页顶级轮播图',
                'verbose_name_plural': '首页顶级轮播图',
                'db_table': 'hahaha_topbanner',
            },
        ),
        migrations.DeleteModel(
            name='T',
        ),
    ]
