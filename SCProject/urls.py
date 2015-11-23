from django.conf.urls import include, url
from django.contrib import admin
from CollegeEventsApp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'SCProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventsApp/', include('CollegeEventsApp.urls')),
    url(r'^eventsAPI/events/$', views.eventsAPI, name='eventsAPI'),
    url(r'^eventsAPI/events/(?P<username>.+)/$', views.eventsUserAPI, name='eventsUserAPI'),
    url(r'^eventsUnsafeAPI/events/(?P<username>.+)/$', views.eventsUnsafeUserAPI, name='eventsUnsafeUserAPI'),
]
