import uuid
import os
from django.db import models
from ckeditor.fields import RichTextField
from django_cleanup import cleanup
from django.utils.text import slugify


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
    lock = models.BooleanField(default=False,help_text="隱藏專案")
    created_at = models.DateTimeField(auto_now_add=True,help_text='創建日期')
    updated_at = models.DateTimeField(auto_now=True,help_text='更新日期')
    slug = models.SlugField("網址識別碼", max_length=200,unique=True,allow_unicode=True,blank=True)

    def __str__(self):
        return self.c_title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.c_title, allow_unicode=True)
            slug_candidate = base
            counter = 1

            # 只檢查「其他」的 slug 是否重複
            qs = Project.objects.filter(slug=slug_candidate)
            if self.pk:
                qs = qs.exclude(pk=self.pk)

            while qs.exists():
                counter += 1
                slug_candidate = f"{base}-{counter}"
                qs = Project.objects.filter(slug=slug_candidate)
                if self.pk:
                    qs = qs.exclude(pk=self.pk)

            self.slug = slug_candidate

        super().save(*args, **kwargs)



