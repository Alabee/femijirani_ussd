from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import AdditionalInfo

# Create your views here.
def index(request):
	return render(request, 'web/home.html')

def donate(request):
	return render(request, 'web/donate.html')

def register(request):
	if request.method == 'POST':
		form = AdditionalInfo(request.POST) #instantiate the form and pass in the post data
		
		if form.is_valid(): #check whether data passed in is okay
			form.save()

		return redirect('register')

	else:
		form = AdditionalInfo()
	
	context = {'form': form}
	return render(request, 'registration/register.html', context)

def test(request):
	return render(request, 'web/test.html')