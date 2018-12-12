from rest_framework import serializers
from ussd.models import Jirani
from web.models import Agent
from django.contrib.auth.models import User

class JiraniSerializer(serializers.ModelSerializer):

	class Meta:
		model = Jirani
		fields = '__all__'
		#fields = ("firstName", "phoneNumber")  what to use when one wants to send back specific fields
		
class AgentSerializer(serializers.ModelSerializer):

	class Meta: 
		model = User
		fields = ("first_name", "last_name", "email", "username", "password")