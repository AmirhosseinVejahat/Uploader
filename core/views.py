# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from django.utils.crypto import get_random_string
from django.views.decorators.http import require_POST

def index(request):
    items = Course.objects.all()
    context = { 'items': items }
    return render(request,'core/index.html',context)


def course(request,topic_name):
    items = Course.objects.filter(topic__name=topic_name)
    context = {
        'items': items ,
        'topic_name': topic_name ,


                }
    return render(request,'core/course.html',context)

def getUserInfo(request):
    context = {}
    if 'token' in request.POST :
        pass



@csrf_exempt
@require_POST
def reset_token(request):
    context = {}

    if 'username' in request.POST and 'password' in request.POST :
        user_obj = User.objects.get(username=request.POST['username'])
        this_password = user_obj.password
        if this_password == request.POST['password']:
            token_string = get_random_string(length=24)
            token_obj = Token.objects.filter(user__username=request.POST['username']).update(token=token_string)
            context['token'] = token_string
            context['result'] = 'ok'
        else:
            context['result'] = 'error'

    return JsonResponse(context,encoder=JSONEncoder)




@csrf_exempt
def register(request):

    context = {}

    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        this_username = request.POST["username"]
        this_password = request.POST["password"]
        this_email = request.POST["email"]

        if not User.objects.filter(username=this_username).exists():
            user_obj = User.objects.create(username = this_username, password = this_password, email = this_email)
            token_string = get_random_string(length=24)
            token_obj = Token.objects.create(user=user_obj,token=token_string)
            context["token"] = token_string
            context["result"] = "ok"
        else:
            context["message"] = "This username already exists please use another username"
            context["result"] = "error"
    else:
        context["message"] = "insufficient variables"
        context["result"] = "error"

    return JsonResponse(context,encoder=JSONEncoder)


@csrf_exempt
def test(request):

    data = request.POST
    token = data['token']
    author = User.objects.filter(token__token=token).get()
    Course.objects.create(topic=data['topic'], author=author, level=data['level'], file=data['file'], img=data['img'], description=data['description'], link=data['link'])
    context = {}
    context["status"] = "ok"
    return JsonResponse(context,encoder=JSONEncoder)


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
