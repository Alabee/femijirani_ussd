from rest_framework import serializers
from ussd.models import Jirani
from web.models import AgentCredential

class JiraniSerializer(serializers.ModelSerializer):

	class Meta:
		model = Jirani
		fields = '__all__'
		#fields = ("firstName", "phoneNumber")  what to use when one wants to send back specific fields
		
class AgentCredentialSerializer(serializers.ModelSerializer):

	class Meta: 
		model = AgentCredential
		fields = '__all__'