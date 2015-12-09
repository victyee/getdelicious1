from django.shortcuts import render

# Create your views here.

def about_us(request):
	context = {}
	return render(request, 'footerpages/about.html', context)


def faq(request):
	context = {}
	return render(request, 'footerpages/faq.html', context)


def privacy(request):
	context = {}
	return render(request, 'footerpages/privacy.html', context)


def terms(request):
	context = {}
	return render(request, 'footerpages/terms.html', context)

