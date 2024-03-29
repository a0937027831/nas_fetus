from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('sendmessage',views.sendmessage,name='sendmessage'),
    path('bannerJson',views.banner,name='banner'),
    path('changeDataLockTrue',views.changeDataLockTrue,name='changeDataLockTrue'),
    path('changeDataLockFalse',views.changeDataLockFalse,name='changeDataLockFalse'),
]