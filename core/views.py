# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from core.models import User,Course

def index(request):
    items = Course.objects.all()
    context = { 'items': items }
    return render(request,'core/index.html',context)

def course(request,topic_name):
    items =  Course.objects.filter(topic__name=topic_name)
    for item in items:
        print(item)
    context = {
        'items': items ,
        'topic': topic_name ,


                }
    return render(request,'core/course.html',context)

@csrf_exempt
def test(request):

    data = request.POST
    token = data['token']
    author = User.objects.filter(token__token=token).get()
    Course.objects.create(topic=data['topic'], author=author, level=data['level'], file=data['file'], img=data['img'], description=data['description'], link=data['link'])
    return JsonResponse({

        'status':'ok',


    },encoder=JSONEncoder)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['upload_file']:
        myfile = request.FILES['upload_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')
