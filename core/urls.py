from django.conf.urls import url
from core import views
from django.contrib import admin
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^upload/',views.simple_upload, name="upload"),
    url(r'^course/(?P<topic_name>\w+)',views.course,name="course")


    ]