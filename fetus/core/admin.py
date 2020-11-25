from django.contrib import admin
from .models import Webinfo


class WebinfoAdmin(admin.ModelAdmin):
    list_display = ('phone','adress','email','id')
    list_display_links = ('phone','adress','email')
    readonly_fields = ('updated_at',)

# Register your models here.
admin.site.register(Webinfo,WebinfoAdmin)
