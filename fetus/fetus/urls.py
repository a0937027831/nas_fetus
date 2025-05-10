"""fetus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

def robots_txt_view(request):
    lines = [
        "User-agent: *",
        "Allow: /", # 或者 "Disallow:" 來允許所有
        # 如果您想禁止某些目錄，可以這樣寫：
        "Disallow: /admin/",
        # "Disallow: /private/",
        # 如果您有 sitemap，可以加入這行：
        "Sitemap: https://yuan-pei.com/static/static/xml/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('projects.urls')),
    path('robots.txt', robots_txt_view), # <--- 新增這行來處理 robots.txt
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
