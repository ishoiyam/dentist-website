from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	context = {}
	return render(request, "home.html", context)

def blog_details(request):
	context = {}
	return render(request, "blog_details.html", context)

def blog(request):
	context = {}
	return render(request, "blog.html", context)

def contact(request):
	

	if request.method == "POST":
		message_name = request.POST["message-name"]
		message_email = request.POST["message-email"]
		message = request.POST["message"]

		# send an email
		send_mail(
			"this is the subject",
			message,
			message_email,
			[message_email ],

		)

		context = {
			"message_name": message_name,
			"message-email": message_email,
			"message": message,
		}


		return render(request, "contact.html", context)
	else:
		return render(request, "contact.html")



def about(request):
	return render(request, "about.html", {})

def pricing(request):
	return render(request, "pricing.html", {})

def service(request):
	return render(request, "service.html", {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST["your-name"]
		your_phone = request.POST["your-phone"]
		your_email = request.POST["your-email"]
		your_address = request.POST["your-address"]
		your_schedule = request.POST["your-schedule"]
		your_date = request.POST["your-date"]
		your_message = request.POST["your-message"]

		appointment = f"Name: {your_name} Phone: {your_phone}, Email: {your_email}, Address: {your_address}, Schedule: {your_schedule}, Date: {your_date}, Message: {your_message}."

		send_mail(
			"Appointment Request",
			appointment,
			your_email,
			["dentist@example.com"], # the dentist email
		)

		context = {
			"your_name": your_name,
			"your_phone": your_phone,
			"your_email": your_email,
			"your_address": your_address,
			"your_schedule": your_schedule,
			"your_time": your_time,
			"your_message": your_message,
		}

		return render(request, "appointment.html", context)
	else:
		return render(request, "home.html")