from rest_framework import serializers
from ussd.models import Jirani

class JiraniSerializer(serializers.ModelSerializer):

	class Meta:
		model = Jirani
		fields = '__all__'
		#fields = ("firstName", "phoneNumber")  what to use when one wants to send back specific fields
		