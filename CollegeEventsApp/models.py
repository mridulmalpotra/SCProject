from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	roll_no = models.CharField(primary_key=True, max_length=10)
	ECE = 'ECE'
	CSE = 'CSE'
	streamChoices = (
		(ECE, 'Electronics'),
		(CSE, 'Computer Science'),
	)
	stream = models.CharField(max_length=3, choices=streamChoices, default=CSE)
	batch = models.CharField(max_length=4)
	def __unicode__(self):
		userData = User.objects.get(pk=self.user_id)
		res = '{"Name" : "' + str(userData.first_name) + " " + str(userData.last_name) + '", "Roll No" : "' + str(self.roll_no) + '", "Email" : "' + str(userData.email)
		res = res + '", "Stream" : "' + str(self.stream) + '", "Batch" : "' + str(self.batch) + '"}'
		return res 

	def get_name(self):
		userData = User.objects.get(pk=self.user_id)
		return userData.first_name + " " + userData.last_name

class Events(models.Model):
	eventid = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=50)
	eventDescription = models.CharField(max_length=200)
	eventDate = models.CharField(max_length=10)
	eventTime = models.CharField(max_length=10)
	userWhoPosted = models.ForeignKey(UserProfile, db_index=True)

	def __unicode__(self):
		postedby = UserProfile.objects.get(pk=self.userWhoPosted_id)
		name = User.objects.get(pk=postedby.user_id).first_name + " " + User.objects.get(pk=postedby.user_id).first_name;
		res = '{"EventID" : ' + str(self.eventid) + ', "Event Name" : "' + str(self.eventName) + '", "Event Description" : "' + str(self.eventDescription)
		res = res + '", "Event Date" : "' + str(self.eventDate) + '", "Event Time" : "' + str(self.eventTime) + '", "Posted By" : "' + str(name) + '"}'
		return res
