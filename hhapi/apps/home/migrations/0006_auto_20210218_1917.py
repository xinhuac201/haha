# Generated by Django 2.2.2 on 2021-02-18 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210218_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotbanner',
            options={'verbose_name': '首页热门景点轮播图', 'verbose_name_plural': '首页热门景点轮播图'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '首页分类轮播图标签', 'verbose_name_plural': '首页分类轮播图标签'},
        ),
        migrations.AlterModelOptions(
            name='tagbanner',
            options={'verbose_name': '首页分类轮播图', 'verbose_name_plural': '首页分类轮播图'},
        ),
    ]
