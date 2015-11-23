"""
Specifies the Regex Matching patterns for the main Django backend.
URL Specified is checked with these patterns and subsequent URL
files are referred inside application directory.
"""

from django.conf.urls import include, url
from django.contrib import admin
from CollegeEventsApp import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'SCProject.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventsApp/', include('CollegeEventsApp.urls')),
    url(r'^eventsAPI/events/$', views.eventsAPI, name='eventsAPI'),
    url(r'^eventsAPI/create/(?P<eventName>.+)/(?P<eventDescription>.+)/(?P<date>.+)/(?P<time>.+)$', \
    	views.create_event_API, name='create_event_API'),
    url(r'^eventsAPI/registerUser/(?P<first_name>.+)/(?P<last_name>.+)/(?P<username>.+)/(?P<email>.+)/(?P<rollno>.+)/(?P<batch>.+)/(?P<password>.+)$', \
    	views.create_user_API, name='create_user_API'),
    url(r'^eventsAPI/events/(?P<username>.+)/$', views.eventsUserAPI, name='eventsUserAPI'),
    url(r'^eventsUnsafeAPI/events/(?P<username>.+)/$', views.eventsUnsafeUserAPI, \
    	name='eventsUnsafeUserAPI'),
]
