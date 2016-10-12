from django.conf.urls import patterns, include, url
from hosttracker import views

urlpatterns = patterns('',
    ('^login/$', views.login),
)
