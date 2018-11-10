from django.db import models

# Create your models here.
class Donor(models.Model):
	phoneNumber = models.CharField(max_length=255)
	amount = models.CharField(max_length=255)

	def __str__(self):
		return self.phoneNumber

class Jirani(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	ID = models.CharField(max_length=20)
	DOB = models.CharField(max_length=20)
	phoneNumber = models.CharField(max_length=20)
	county = models.CharField(max_length=20)
	town = models.CharField(max_length=20)
	estate = models.CharField(max_length=20)
	landmark = models.CharField(max_length=20)
	piecesRequested = models.CharField(max_length=20)

	def __str__(self):
		return self.firstName