# Generated by Django 2.2.2 on 2021-02-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20210219_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='price',
            field=models.IntegerField(default=0, verbose_name='价格'),
        ),
        migrations.AddField(
            model_name='route',
            name='sort_num',
            field=models.SmallIntegerField(default=0, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='route',
            name='map',
            field=models.ImageField(blank=True, help_text='图片长宽固定的', null=True, upload_to='banner/map/', verbose_name='上传路线图片'),
        ),
    ]