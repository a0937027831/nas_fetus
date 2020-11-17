import uuid
import os
from django.db import models
from ckeditor.fields import RichTextField
from django_cleanup import cleanup

def image_file_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/projects/',filename)

def preview_img_file_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/projects/preview/',filename)



class ImageInfo(models.Model):
    title = models.CharField(max_length=200,default='',help_text='照片標題(例:案子名稱_臥室1...)')
    image = models.ImageField(upload_to = image_file_path,help_text='照片')

    def __str__(self):
        return self.title

class Tags(models.Model):
    tag = models.CharField(max_length=20,default='',help_text='案子類別(自己看的分類)')
    c_title = models.CharField(max_length=30,default='',help_text='中文名子(顯示在作品列表)')
    e_title = models.CharField(max_length=30,default='',help_text='英文名子(顯示在作品列表)')
    def __str__(self):
        return self.tag

class Project(models.Model):
    c_title = models.CharField(max_length=30,default='',help_text='中文標題')
    e_title = models.CharField(max_length=30,default='',help_text='英文標題')
    images = models.ManyToManyField('ImageInfo',help_text='案子照片(複選) 按住ctrl複選')
    preview_img = models.ImageField(upload_to = preview_img_file_path,default='',help_text = '外部顯示圖片(寬:2667 高:1440)')
    project_tag = models.ForeignKey(Tags,related_name='p_tag',on_delete = models.CASCADE,default='', null=True,help_text='案子類別')
    body = RichTextField(blank=True,null=True,help_text='案子文字敘述')
    created_at = models.DateTimeField(auto_now_add=True,help_text='創建日期')
    updated_at = models.DateTimeField(auto_now=True,help_text='更新日期')
    def __str__(self):
        return self.c_title



