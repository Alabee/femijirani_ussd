from django.db import models

# Create your models here.
class Agent(models.Model):
	agent_id = models.CharField(max_length=10)
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	ID = models.CharField(max_length=255)
	phoneNumber = models.CharField(max_length=255)

	def __str__(self):
		return self.agent_id + ":" + self.firstName

class AgentCredential(models.Model):
	agent = models.ForeignKey(Agent, on_delete = models.CASCADE)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=10)
