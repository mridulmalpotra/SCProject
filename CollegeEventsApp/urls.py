from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signin/$', views.login_view, name='login_view'),
	url(r'^signup/$', views.signup_view, name='signup_view'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^dashboard/create/$', views.create_event, name='create_event'),
	url(r'^dashboard/viewall/$', views.view_all_events, name='view_all_events'),
]