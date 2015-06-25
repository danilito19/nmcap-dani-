from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.projects),
    url(r'^search/$', views.search),
]

