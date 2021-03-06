# Generated by Django 3.0.11 on 2020-11-22 13:01

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinfo',
            name='about_title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='關於我 標題顏色', max_length=18),
        ),
        migrations.AddField(
            model_name='webinfo',
            name='contact_title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='聯絡我 標題顏色', max_length=18),
        ),
        migrations.AddField(
            model_name='webinfo',
            name='home_title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='主頁 標題顏色', max_length=18),
        ),
        migrations.AddField(
            model_name='webinfo',
            name='service_title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='服務 標題顏色', max_length=18),
        ),
        migrations.AddField(
            model_name='webinfo',
            name='work_list_title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='作品列表 標題顏色', max_length=18),
        ),
        migrations.AddField(
            model_name='webinfo',
            name='work_title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='作品分類 標題顏色', max_length=18),
        ),
    ]
