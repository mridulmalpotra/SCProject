from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	roll_no = models.CharField(max_length=10)
	# name = models.CharField(max_length=20)
	# email = models.EmailField(max_length=50)
	# username = models.CharField(max_length=10)
	ECE = 'ECE'
	CSE = 'CSE'
	streamChoices = (
		(ECE, 'Electronics'),
		(CSE, 'Computer Science'),
	)
	stream = models.CharField(max_length=3, choices=streamChoices, default=CSE)
	batch = models.CharField(max_length=4)
	
	def __unicode__(self):
		res = '{"Name" : "' + str(self.name) + '", "Roll No" : "' + str(self.roll_no) + '", "Email" : "' + str(self.email)
		res = res + '", "Stream" : "' + str(self.stream) + '", "Batch" : "' + str(self.batch) + '"}'
		return res 

class Events(models.Model):
	eventid = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=50)
	eventDescription = models.CharField(max_length=200)
	eventDate = models.DateTimeField('Event Date/Time')
	userWhoPosted = models.ForeignKey(UserProfile, db_index=True)

	def __unicode__(self):
		res = '{"EventID" : ' + str(self.eventid) + ', "Event Name" : ' + str(self.eventName) + ', "Event Description" : ' + str(self.eventDescription)
		res = res + ', "Event Date" : ' + str(self.eventDate) + '}'
		return res
