import uuid
import os
from django.db import models
from django_cleanup import cleanup

def image_file_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/banner/',filename)

class Banner(models.Model):
    image1 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面1 寬:450px 高:450px')
    image2 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面2 寬:450px 高:450px')
    image3 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面3 寬:450px 高:450px')
    image4 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面4 寬:450px 高:450px')
    image5 = models.ImageField(upload_to = image_file_path,blank=True,default='',help_text='封面5 寬:450px 高:450px')
    updated_at = models.DateTimeField(auto_now=True,help_text='更新日期')

    class Meta:
        ordering = ('-updated_at',)

class CustomerContact(models.Model):
    name = models.CharField(max_length=200,default='',help_text='姓名')
    title = models.CharField(max_length=200,default='',help_text='主旨')
    email = models.CharField(max_length=200,default='',help_text='信箱')
    phone = models.CharField(max_length=200,default='',help_text='手機')
    message = models.CharField(max_length=200,default='',help_text='訊息')

    def __str__(self):
        return self.title
