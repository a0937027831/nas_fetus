from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Project,Tags
from core.models import Webinfo

# Create your views here.

def straddspace(string):
    title = ''
    i = 0
    for char in string:
        if(i == len(string)-1):
            title += char
        else:
            title += (char+' ')
        i+=1
    return title


def works(request):
    webinfo = get_object_or_404(Webinfo,pk=1)
    tags = Tags.objects.all()
    for tag in tags:
        tag.c_title = straddspace(tag.c_title)
    context = {'webinfo':webinfo,'tags':tags}
    return render(request,'works.html',context)


def works_list(request,tag_id):
    webinfo = get_object_or_404(Webinfo,pk=1)
    projects = get_list_or_404(Project,project_tag__id = tag_id)
    tag = get_object_or_404(Tags,pk=tag_id)
    context = {'webinfo':webinfo,'projects':projects,'tag':tag}
    return render(request,'work_list.html',context)

def works_detail(request,tag_id,project_id):
    print('tag_id :'+ tag_id)
    print('project_id :'+project_id)
    project_id = int(project_id)
    projects = get_list_or_404(Project,project_tag__id = tag_id)
    context = {'projects': projects,'project_id':project_id}
    return render(request,'work_detail.html',context)


