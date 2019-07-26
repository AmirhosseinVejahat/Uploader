from django.conf.urls import url
from core import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^upload/', views.simple_upload, name="upload"),
    url(r'^test/',views.test,name="test"),
    url(r'^course/(?P<topic_name>\w+)',views.course,name="course")


    ]