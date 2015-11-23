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
	return HttpResponseRedirect('/eventsApp/')

@login_required(login_url='/eventsApp/signin')
@csrf_protect
def dashboard(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		if user.is_superuser:
			return render_to_response('admin_dashboard.html', context_instance=RequestContext(request))
		return render_to_response('dashboard.html', context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/eventsApp/signin', {'msg' : "Please login to continue"})

@login_required(login_url='/eventsApp/signin')
@csrf_protect
def user_view(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		if user.is_superuser:
			user = UserProfile.objects.all()
			return render_to_response('admin_all_users.html', {'data' : user}, context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/eventsApp/dashboard');

@login_required(login_url='/eventsApp/signin')
@csrf_protect
def profile(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			user = User.objects.get(username=request.user)
			profile = UserProfile.objects.get(user=user.pk)
			return render_to_response('profile.html', {'data' : profile}, context_instance=RequestContext(request))
		if request.method == 'POST':
			user = User.objects.get(username=request.user)
			profile = UserProfile.objects.get(user=user.pk)
			print request.POST.get('test', False)
			if request.POST.get('test', False):
				return render_to_response('change_password.html', {'data': profile}, context_instance=RequestContext(request))
			password = request.POST['password']
			password_confirmation = request.POST['password_confirmation']
			if password != password_confirmation:
				return render_to_response('signup.html', {'msg' : "Passwords doesn't match"}, context_instance=RequestContext(request))
			else:
				user.set_password(password)
				user.save()
				return HttpResponseRedirect('/eventsApp/dashboard')
	else:
		return HttpResponseRedirect('/eventsApp/signin')

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
			user = User.objects.get(username=request.user)
			if user.is_superuser:
				return render_to_response('admin_all_events.html', {'data' : event}, context_instance=RequestContext(request))
			else:
				return render_to_response('view_all_events.html', {'data' : event}, context_instance=RequestContext(request))
		if request.method == 'POST':
			user = User.objects.get(username=request.user)
			if user.is_superuser:
				if request.POST.get('eventId', False):
					eventid = request.POST['eventId']
					delete = False
					confirm = False
					editFin = False
					if request.POST.get('delete', False):
						delete = True
					if delete:
						if request.POST.get('confirm', False):
							event = Events.objects.get(eventid=eventid).delete()
							event = Events.objects.all()
							return render_to_response('admin_all_events.html', {'data' : event}, context_instance=RequestContext(request))
						else:
							event = Events.objects.get(eventid=eventid)
							return render_to_response('confirmation.html', {'data' : event}, context_instance=RequestContext(request))
					else:
						if request.POST.get('editFin', False):
							eventDescription = request.POST['eventDescription']
							eventDate = request.POST['date']
							eventTime = request.POST['time']
							Events.objects.filter(eventid=eventid).update(eventDescription=eventDescription, eventDate=eventDate, eventTime=eventTime)
							event = Events.objects.all()
							return render_to_response('admin_all_events.html', {'data' : event}, context_instance=RequestContext(request))
						else:
							event  = Events.objects.get(eventid=eventid)
							return render_to_response('edit_event.html', {'data' : event}, context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/eventsApp/dashboard')
	else:
		return HttpResponseRedirect('/eventsApp/signin')

@login_required(login_url='eventsApp/signin')
@csrf_protect
def view_my_events(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			user = User.objects.get(username=request.user)
			profile = UserProfile.objects.get(user=user.pk)
			event = Events.objects.filter(userWhoPosted=profile.pk)
			return render_to_response('my_event.html', {'data' : event}, context_instance=RequestContext(request))
		if request.method == 'POST':
			if request.POST.get('eventId', False):
				eventid = request.POST['eventId']
				delete = False
				confirm = False
				editFin = False
				if request.POST.get('delete', False):
					delete = True
				if delete:
					if request.POST.get('confirm', False):
						event = Events.objects.get(eventid=eventid).delete()
						user = User.objects.get(username=request.user)
						profile = UserProfile.objects.get(user=user.pk)
						event = Events.objects.filter(userWhoPosted=profile.pk)
						return render_to_response('my_event.html', {'data' : event}, context_instance=RequestContext(request))
					else:
						event = Events.objects.get(eventid=eventid)
						return render_to_response('confirmation.html', {'data' : event}, context_instance=RequestContext(request))
				else:
					if request.POST.get('editFin', False):
						eventDescription = request.POST['eventDescription']
						eventDate = request.POST['date']
						eventTime = request.POST['time']
						print eventDescription, eventDate, eventTime
						Events.objects.filter(eventid=eventid).update(eventDescription=eventDescription, eventDate=eventDate, eventTime=eventTime)
						user = User.objects.get(username=request.user)
						profile = UserProfile.objects.get(user=user.pk)
						event = Events.objects.filter(userWhoPosted=profile.pk)
						return render_to_response('my_event.html', {'data' : event}, context_instance=RequestContext(request))
					else:
						event  = Events.objects.get(eventid=eventid)
						return render_to_response('edit_event.html', {'data' : event}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/eventsApp/signin')

def eventsAPI(request):
	if request.method == 'GET':
		events = Events.objects.all()
		data = "["
		for e in events:
			print str(e)
			data += str(e) + ","
			print data
		if data != '[':
			data = data[:-1] + ']'
		else:
			data += ']'
		print data
		retVal = '{"status" : true, "events" : ' + data + ', "message" : null}'
		return HttpResponse(retVal)
	if request.method == 'POST':
		return HttpResponse("Not Allowed.")

def eventsUserAPI(request, username):
	if request.method == 'GET':
		try:
			user = User.objects.get(username=username)
			profile = UserProfile.objects.get(user=user.pk)
			events = Events.objects.filter(userWhoPosted=profile.pk)
			data = "["
			for e in events:
				print str(e)
				data += str(e) + ","
				print data
			if data != '[':
				data = data[:-1] + ']'
			else:
				data += ']'
			print data
			retVal = '{"status" : true, "events" : ' + data + ', "message" : null}'
			return HttpResponse(retVal)
		except:
			return HttpResponse("No events found")
	if request.method == 'POST':
		return HttpResponse("Not Allowed.")

def eventsUnsafeUserAPI(request, username):
	if request.method == 'GET':
		try:
			events = Events.objects.raw('SELECT * FROM CollegeEventsApp_events where userWhoPosted_id=\"' + username + '\"')
			data = "["
			for e in events:
				print str(e)
				data += str(e) + ","
				print data
			if data != '[':
				data = data[:-1] + ']'
			else:
				data += ']'
			print data
			retVal = '{"status" : true, "events" : ' + data + ', "message" : null}'
			return HttpResponse(retVal)
		except:
			return HttpResponse("No events found")
	if request.method == 'POST':
		return HttpResponse("Not Allowed.")	


