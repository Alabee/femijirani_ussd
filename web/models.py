from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(User):
	agent_id = models.CharField(max_length=255)
	ID = models.CharField(max_length=255)
	phoneNumber = models.CharField(max_length=255)

	def __str__(self):
		return self.agent_id 

