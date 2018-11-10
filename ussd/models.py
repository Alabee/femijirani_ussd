from django.db import models

# Create your models here.
class Donor(models.Model):
	phoneNumber = models.CharField(max_length=255)
	amount = models.CharField(max_length=255)

	def __str__(self):
		return self.phoneNumber

class Jirani(models.Model):
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	ID = models.CharField(max_length=255)
	phoneNumber = models.CharField(max_length=255)
	county = models.CharField(max_length=255)
	town = models.CharField(max_length=255)
	estate = models.CharField(max_length=255)
	landmark = models.CharField(max_length=255)
	peopleApplied = models.CharField(max_length=255)#will be sorted to be in a different table

	def __str__(self):
		return self.firstName


#The max_length limits should be revised