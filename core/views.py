# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from django.utils.crypto import get_random_string
from django.views.decorators.http import require_POST
from .forms import UploadFileForm
from django.http import HttpResponseRedirect


def handle_uploaded_file(author, topic, file):
    dir_path = os.path.join('media', 'video', author, topic)
    file_path = os.path.join(dir_path,file.name)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    with open(file_path,'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def upload(request):
    url = ''
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            author = User.objects.get(id=request.POST["author"])
            topic = Topics.objects.get(id=request.POST["topic"])
            handle_uploaded_file(author.username, topic.name, request.FILES['file'])
            # TODO : Check File Uploaded Successfully
            url = 'core/upload.html'
            context = {'form': form,
                       'uploaded_file': True,
                       }
            return render(request,url,context)
    else:
        form = UploadFileForm()
        url = 'core/upload.html'
        context = {'form': form}
    return render(request, url, context)


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
    url = 'core/register.html'
    print(request.POST)
    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        this_username = request.POST["username"]
        this_password = request.POST["password"]
        this_email = request.POST["email"]
        if not User.objects.filter(username=this_username).exists():
            user_obj = User.objects.create(username = this_username, password = this_password, email = this_email)
            token_string = get_random_string(length=24)
            token_obj = Token.objects.create(user=user_obj,token=token_string)
            context["token"] = token_string
            context["result"] = True
        else:
            context["message"] = "This username already exists please use another username"
            context["result"] = "UserExists"
    else:
        context["message"] = ""
        context["result"] = ""

    return render(request,url,context)


