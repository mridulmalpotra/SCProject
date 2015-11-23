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
	url(r'^dashboard/myevents/$', views.view_my_events, name='view_my_events'),
	url(r'^dashboard/profile/$', views.profile, name='profile'),
	url(r'^dashboard/logout/$', views.logout_view, name='logout_view'),
	url(r'^dashboard/viewUsers/$', views.user_view, name='user_view'),
]