from django.urls import path
from . import views

urlpatterns = [
    # 首頁作品列表
    path('works/', views.works, name='works'),
    # 某個分類底下的作品清單
    path('works/<int:tag_id>/', views.works_list, name='works_list'),
    # 單一作品詳情，用 slug （改成 str，可接受中文）
    path(
        'works/<int:tag_id>/<str:project_slug>/',
        views.works_detail,
        name='works_detail'
    ),
]