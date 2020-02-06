import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	if request.method == "POST":
		#do stuff
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']
		
		#send email
		send_mail(
			'Crystal Tutor Message From: ' + your_name, #subject
			'Name: ' + your_name + '\nPhone :' + your_phone + '\nAddress: ' + your_address + '\n Email: ' + your_email + '\nTime slot: ' + your_time + '\n\nMessage: ' + your_message, #message
			your_email, #from email
			['crystaltutorwebsite@gmail.com'], #to email
			fail_silently=False,
			)

		return render(request, 'home.html', {'your_message':your_message})

	else:

		return render(request, 'home.html', {})