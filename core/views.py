# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.models import Movie
from django.core.files.storage import FileSystemStorage


def index(request):
    items = Movie.objects.all()
    return render(request,'core/index.html',{
        'items' : items,
    })

def item_details(request):
    items = Movie.objects.get(id=id)
    return render(request,'core/index.html',{

        'items' : items,

    })


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