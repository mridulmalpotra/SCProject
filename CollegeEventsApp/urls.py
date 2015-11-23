from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signin/$', views.login_view, name='login_view'),
	url(r'^signup/$', views.signup_view, name='signup_view')
]