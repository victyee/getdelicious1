from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.conf import settings
from .forms import ContactUsForm

# Create your views here.

def contact(request):
	contact_us_form = ContactUsForm(request.POST or None)
	context = {"contact_us_form": contact_us_form }
	if request.method == "POST":
		if contact_us_form.is_valid():
			new_query = contact_us_form.save()
			messages.success(request, "Thank you, your query has been successfully sent. We'll get back to you soon.")
			return HttpResponseRedirect("/")
		else:
			messages.error(request, "All fields are required.")


	return render(request, 'contact/contact.html', context)
