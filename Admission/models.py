from django.db import models

# Create your models here.

class Students(models.Model):
	def __str__(self):
		return self.name
	Enrollment = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=100)
	contact = models.IntegerField(default=0)
	age = models.IntegerField(default=18)
	avatar = models.ImageField('profile picture', upload_to='static/Admission/profiles/', null=True, blank=True)

class chat(models.Model):
	def __str__(self):
		return self.senderemail+" to "+self.receiveremail
	sender = models.CharField(max_length=500)
	receiver = models.CharField(max_length=500)
	message = models.CharField(max_length=100000)
	senderemail = models.CharField(max_length=500,default=1)
	receiveremail = models.CharField(max_length=500,default=1)
