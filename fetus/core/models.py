import uuid
import os
from django.db import models
from django_cleanup import cleanup
from colorfield.fields import ColorField


def image_file_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/web_bg/',filename)


# Create your models here.
class Webinfo(models.Model):
    phone = models.CharField(max_length=200,default='',help_text='手機或電話')
    adress = models.CharField(max_length=200,default='',help_text='公司地址')
    email = models.EmailField(max_length = 100,default='',help_text='公司信箱')
    year = models.CharField(max_length=10,default='',help_text='今年年分')
    home_bg = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='主頁背景')
    work_bg = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='作品分類背景')
    work_list_bg = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='作品列表背景')
    service_bg = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='服務背景')
    about_bg = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='關於我背景')
    contact_bg = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='聯絡我背景')
    home_title_color = ColorField(default="#FFFFFF",help_text='主頁 標題顏色')
    work_title_color = ColorField(default="#FFFFFF",help_text='作品分類 標題顏色')
    work_list_title_color = ColorField(default="#FFFFFF",help_text='作品列表 標題顏色')
    service_title_color = ColorField(default="#FFFFFF",help_text='服務 標題顏色')
    about_title_color = ColorField(default="#FFFFFF",help_text='關於我 標題顏色')
    contact_title_color = ColorField(default="#FFFFFF",help_text='聯絡我 標題顏色')
    works_text_color = ColorField(default="#FFFFFF",help_text='作品分類 下方選擇顏色')
    about_title_text_color = ColorField(default="#FFFFFF",help_text='關於我 下方標題選擇顏色')
    about_text_color = ColorField(default="#FFFFFF",help_text='關於我 下方文字顏色')
    service_title_text_color = ColorField(default="#FFFFFF",help_text='服務 下方標題文字顏色')
    service_text_color = ColorField(default="#FFFFFF",help_text='服務 下方文字顏色')
    footer_text_color = ColorField(default="#FFFFFF",help_text='網頁最下方文字顏色(@2020~)')

    updated_at = models.DateTimeField(auto_now=True,help_text='更新日期')

    class Meta:
        ordering = ('-updated_at',)

