from django.urls import path
from . import views

urlpatterns = [
    path('works',views.works,name='works'),
    path('works/<int:tag_id>',views.works_list,name='works_list'),
    path('works_detail/<str:tag_id>/<str:project_id>',views.works_detail,name='works_detail')
]