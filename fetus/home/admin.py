from django.contrib import admin
from .models import Banner,CustomerContact

# Register your models here.

class CustomerContactAdmin(admin.ModelAdmin):
    list_display = ('name','title','phone','email')
    list_display_links = ('name','title','phone','email')

admin.site.register(Banner)
admin.site.register(CustomerContact,CustomerContactAdmin)