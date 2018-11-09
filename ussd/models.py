from django.db import models

# Create your models here.
class Donor(models.Model):
	phoneNumber = models.CharField(max_length=10)
	amount = models.CharField(max_length=20)

class Jirani(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	ID = models.CharField(max_length=20)
	DOB = models.CharField(max_length=20)
	phoneNumber = models.CharField(max_length=20)
	county = models.CharField(max_length=20)
	town = models.CharField(max_length=20)
	estate/village = models.CharField(max_length=20)
	landmark = models.CharField(max_length=20)
	piecesRequested = models.CharField(max_length=20)