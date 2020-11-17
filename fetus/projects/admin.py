from django.contrib import admin
from .models import ImageInfo,Tags,Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('c_title','e_title','project_tag','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')

class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag','c_title','e_title','id')
    list_display_links = ('tag','c_title','e_title')
    readonly_fields = ('id',)


admin.site.register(ImageInfo)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Project,ProjectAdmin)