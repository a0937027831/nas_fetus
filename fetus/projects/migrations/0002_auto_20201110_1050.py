# Generated by Django 3.0.10 on 2020-11-10 10:50

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='preview_img',
            field=models.ImageField(default='', help_text='外部顯示圖片(寬:2667 高:1440)', upload_to=projects.models.preview_img_file_path),
        ),
    ]
