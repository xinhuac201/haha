# Generated by Django 2.2.2 on 2021-02-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_auto_20210220_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='strength',
            field=models.FloatField(default=0, verbose_name='体能系数'),
        ),
    ]
