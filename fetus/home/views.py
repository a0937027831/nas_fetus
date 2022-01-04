import re
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from core.models import Webinfo
from fetus import projects
from .models import Banner,CustomerContact
from .serializers import BannerSerializer
from projects.models import Project
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
    webinfo = Webinfo.objects.all()[0]
    context = {'webinfo': webinfo}
    return render(request,'home.html',context)


def about(request):
    webinfo = Webinfo.objects.all()[0]
    context = {'webinfo': webinfo}
    return render(request,'about.html',context)

def services(request):
    webinfo = Webinfo.objects.all()[0]
    context = {'webinfo': webinfo}
    return render(request,'services.html',context)

def contact(request):
    webinfo = Webinfo.objects.all()[0]
    context = {'webinfo': webinfo}
    return render(request,'contact.html',context)

def changeDataLockTrue(requset):
    all_Project = Project.objects.all()
    all_Project.update(lock = True)
    return render(requset)

def changeDataLockFalse(requset):
    all_Project = Project.objects.all()
    all_Project.update(lock = False)
    return render(requset)




@require_http_methods(["POST"])
def sendmessage(request):
    name = request.POST['name']
    title = request.POST['title']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    values = {'name':name,'title':title,'phone':phone,'message':message}

    try:
        validate_email(email)
    except ValidationError:
        messages.warning(request,'信箱格式錯誤!')
        return redirect('contact')

    # Sena email
    send_mail(
        title,
        message+'\n聯絡方式 :'+phone + "\nemail :"+email,
        'from@yourdjangoapp.com',
        ['andyfamrykames@gmail.com'],
        fail_silently=False
    )
    CustomerContact.objects.create(name=name,title=title,email=email,phone=phone,message=message)
    messages.success(request,'成功送出!')
    return redirect('contact')


@require_http_methods(["GET"])
def banner(request):
    jsonBanner = Banner.objects.all()[0]
    jsonBanner = BannerSerializer(jsonBanner,many=False)
    return JsonResponse(jsonBanner.data,safe=False)
