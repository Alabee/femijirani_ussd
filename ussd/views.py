from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

#importing tables to save data
from .models import Donor, Jirani


# Create your views here.

@csrf_exempt
@api_view(['POST'])
def index(request):
	text = request.POST['text']
	phoneNumber = request.POST['phoneNumber']

	#Considering text contains the responses given by the user as a string separated by asterisk e.g "1*500" or "2*Jane"
	#We use the asterisk to separate the responses and store them in an array
	user_responses = text.split('*')

	#level 1
	if text == "":
		response = "CON Welcome to Femi-jirani\nPlease select an option to proceed\n1. Donate\n2. Apply for sanitary towels"
	
	#level 2	
	elif text == "1":
		response = "CON Please enter amount to donate"

	elif text == "2":
		response = "CON Please enter the following details\nFirst name"

	#level 3
	elif user_responses[1] != "" and len(user_responses) == 2:
		if user_responses[0] == "1":
			response = "CON Please enter M-Pesa pin"

		elif user_responses[0] == "2":
			response = "CON Last name"

	#level 4
	elif user_responses[2] != "" and len(user_responses) == 3:
		if user_responses[0] == "1":
			response = "END Thank you for your donation.\nIt counts."

		elif user_responses[0] == "2":
			response = "CON ID number/DOB(DD/MM/YY)"
	
	#level 5
	elif user_responses[3] != "" and len(user_responses) == 4:
		response = "CON How many people are you applying for?"

	#level 6
	elif user_responses[4] != "" and len(user_responses) == 5:
		response = "CON Help us establish your location\nCounty"
	
	#level 7
	elif user_responses[5] != "" and len(user_responses) == 6:
		response = "CON Town"

	#level 8
	elif user_responses[6] != "" and len(user_responses) == 7:
		response = "CON Estate/Village"

	#level 9
	elif user_responses[7] != "" and len(user_responses) == 8:
		response = "CON Nearest landmark(Primary school/secondary school/hospital/local church"

	#level 10
	elif user_responses[8] != "" and len(user_responses) == 9:
		response = "END Your application has been received.\n Confirmation will be sent to you via text."

	else:
		response = "END Thank you for visiting Femi-jirani!"

	#SAVING DATA TO DATABASE
	if user_responses[0] == "1":
		if len(user_responses) == 3:
			donor = Donor()
			donor.phoneNumber = phoneNumber
			donor.amount = user_responses[1]
			donor.save()

	elif user_responses[0] == "2":
		if len(user_responses) == 9:
			jirani = Jirani()
			jirani.firstName = user_responses[1]
			jirani.lastName = user_responses[2]
			jirani.ID = user_responses[3]
			jirani.peopleApplied = user_responses[4]
			jirani.phoneNumber = phoneNumber
			jirani.county = user_responses[5]
			jirani.town = user_responses[6]
			jirani.estate = user_responses[7]
			jirani.landmark = user_responses[8]
			jirani.save()
			

	return HttpResponse(response, content_type="text/plain")


	'''
	elif len(user_responses) == 1 and text != "1" or "2":
		response = "END Thank you for visiting Femi-jirani"

'''