from django.shortcuts import render, Http404

# Create your views here.

from marketing.forms import EmailForm
from marketing.models import MarketingMessage, Slider


from .models import Product, ProductImage


def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(foodtruck_name__icontains=q)
		context = {'query': q, 'products': products}
		template = 'products/results.html'	
	else:
		template = 'products/home.html'	
		context = {}
	return render(request, template, context)


def home(request):
	user = request.user
	sliders = Slider.objects.all_featured()
	products = Product.objects.all()
	template = 'products/home.html'	

	try:
		truck_name = user.product
		context = {
		"products": products,
		"sliders": sliders,
		"truck_name": truck_name,
		}
		return render(request, template, context)

	except: 
		context = {
		"products": products,
		"sliders": sliders,
		}
		return render(request, template, context)

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
	return render(request, template, context)


def single(request, slug):
	user = request.user
	products = Product.objects.all()
	try:
		product = Product.objects.get(slug=slug)
		print product.get_absolute_url
		# images = product.productimage_set.all() alternate way to get images. need to import ProductImage for this to work
		images = ProductImage.objects.filter(product=product) #need to import ProductImage for this to work
		
		template = 'products/single.html'

		variations = product.variation_set.all()
		print variations
		for i in variations:
			minimum_guests = i.minimum_guests
		context = {'images': images, 'product': product, "minimum_guests": minimum_guests, "products": products}
		return render(request, template, context)
	except:
		raise Http404


def victoria(request):
	state = "Victoria"
	products = Product.objects.all()
	caption = "Victoria - The Place To Be"
	for i in products:
		trucks = Product.objects.filter(operating_state="VIC")

	template = 'products/all.html'
	context = {"state": state,
				"trucks": trucks,
				"caption": caption,
			}
	return render(request, template, context)


def new_south_wales(request):
	state = "New South Wales"
	products = Product.objects.all()
	caption = "New South Wales - The Premier State"
	for i in products:
		trucks = Product.objects.filter(operating_state="NSW")

	template = 'products/all.html'
	context = {"state": state,
				"trucks": trucks,
				"caption": caption,
			}
	return render(request, template, context)


def south_australia(request):
	state = "South Australia"
	products = Product.objects.all()
	caption = "South Australia - The Festive State"
	for i in products:
		trucks = Product.objects.filter(operating_state="SA")
	template = 'products/all.html'
	context = {"state": state,
				"trucks": trucks,
				"caption": caption,
			}
	return render(request, template, context)


def queensland(request):
	state = "Queensland"
	products = Product.objects.all()
	caption = "Queensland - Sunshine State"
	for i in products:
		trucks = Product.objects.filter(operating_state="QLD")

	template = 'products/all.html'
	context = {"state": state,
				"trucks": trucks,
				"caption": caption,
			}
	return render(request, template, context)


def western_australia(request):
	state = "Western Australia"
	products = Product.objects.all()
	caption = "Western Australia - The Golden State"
	for i in products:
		trucks = Product.objects.filter(operating_state="WA")
	template = 'products/all.html'
	context = {"state": state,
				"trucks": trucks,
				"caption": caption,
			}
	return render(request, template, context)