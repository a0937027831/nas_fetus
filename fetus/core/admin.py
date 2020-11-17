from django.contrib import admin
from .models import Webinfo


class WebinfoAdmin(admin.ModelAdmin):
    list_display = ('phone','adress','email')
    list_display_links = ('phone','adress','email')

# Register your models here.
admin.site.register(Webinfo,WebinfoAdmin)
