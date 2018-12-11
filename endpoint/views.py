from django.shortcuts import render, get_object_or_404 #gets the object or returns a 404 if the object oes not exist
from rest_framework.views import APIView #APIView makes the normal views return API response
from rest_framework.response import Response
from rest_framework import status
from ussd.models import Jirani
from web.models import AgentCredential
from .serializers import JiraniSerializer, AgentCredentialSerializer
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
# Setting up a class-based view allows factoring in different types of request for the same thing(POST or GET)


class JiraniList(APIView):

	def get(self, request):
		query = request.GET.get('name')
		jiranis = Jirani.objects.filter(firstName = query)
		serializer = JiraniSerializer(jiranis, many = True)

		return Response(serializer.data)


	def post(self):
		pass

class AgentCredentialDetail(APIView):

	def get(self, request):
		agent = AgentCredential.objects.all()
		serializer = AgentCredentialSerializer(agent, many = True)

		return Response(serializer.data)

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = (username, password)
		login(request, user)

		'''
		if AgentCredential.objects.filter(username=username).exists():
			user = AgentCredential.objects.get(username=username)
			
			if password == user.password:
				return HttpResponse("Access granted")

			else:
				return HttpResponse("Wrong password")
		else:
			return HttpResponse("User does not exist")
		'''

