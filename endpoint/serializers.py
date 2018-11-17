from rest_framework import serializer
from ussd.models import Jirani

class JiraniSeriaizer(serializers.ModelSerializer):

	class Meta:
		model = Jirani
		fields = '__all__'
		#fields = ("firstName", "phoneNumber")  what to use when one wants to send back specific fields
		