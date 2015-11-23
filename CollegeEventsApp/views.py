from .models import *
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db import connections

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))

@csrf_protect
def login_view(request):
	if request.method == 'GET':
		return render_to_response('login_page.html', context_instance=RequestContext(request))
	elif request.method == 'POST':
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = User.objects.get(username=username)
			if user.check_password(password):
				user = authenticate(username=username, password=password)
				login(request, user)
				return HttpResponseRedirect('/eventsApp/dashboard')
			else:
				return render_to_response('login_page.html', {'msg' : "Invalid Login"}, context_instance=RequestContext(request))
		except ObjectDoesNotExist:
			return render_to_response('login_page.html', {'msg' : "This user doesn't exist"}, context_instance=RequestContext(request))

@csrf_protect
def signup_view(request):
	if request.method == 'GET':
		return render_to_response('signup.html', context_instance=RequestContext(request))
	elif request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		rollno = request.POST['rollno']
		batch = request.POST['batch']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']
		if password != password_confirmation:
			return render_to_response('signup.html', {'msg' : "Passwords doesn't match"}, context_instance=RequestContext(request))
		else:
			#todo : accomodate stream. Create dropdown form menu for stream
			user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
			user.save()
			profile = UserProfile.objects.create(user=user, roll_no=rollno, batch=batch)
			profile.save()
			user.save()
			return HttpResponseRedirect('/eventsApp/signin', {'msg' : "Now login to continue"});

@csrf_protect
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/eventsApp')

@login_required(login_url='/eventsApp/signin')
@csrf_protect
def dashboard(request):
	if request.user.is_authenticated():
		return render_to_response('dashboard.html', context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/eventsApp/signin', {'msg' : "Please login to continue"})

@login_required(login_url='eventsApp/signin')
@csrf_protect
def create_event(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			return render_to_response('create_event.html', context_instance=RequestContext(request))
		if request.method == 'POST':
			eventName = request.POST['eventName']
			eventDescription = request.POST['eventDescription']
			date = request.POST['date']
			time = request.POST['time']
			user = User.objects.get(username=request.user)
			profile = UserProfile.objects.get(user=user.pk)
			print profile.roll_no
			print eventName, eventDescription, date, time, user
			event = Events.objects.create(userWhoPosted=profile, eventName=eventName, eventDescription=eventDescription, eventDate=date, eventTime=time)
			event.save()
			profile.save()
			return HttpResponseRedirect('/eventsApp/dashboard')
	else:
		return HttpResponseRedirect('/eventsApp/signin')

@login_required(login_url='eventsApp/signin')
@csrf_protect
def view_all_events(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			event = Events.objects.all()
			return render_to_response('view_all_events.html', {'data' : event}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/eventsApp/signin')
