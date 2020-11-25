from django.contrib import admin
from .models import Banner,CustomerContact

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('updated_at','id')
    readonly_fields = ('updated_at',)

class CustomerContactAdmin(admin.ModelAdmin):
    list_display = ('name','title','phone','email')
    list_display_links = ('name','title','phone','email')

admin.site.register(CustomerContact,CustomerContactAdmin)
admin.site.register(Banner,BannerAdmin)