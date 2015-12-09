import re

from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404, render_to_response
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from .forms import LoginForm, RegistrationForm, UserAddressForm, TruckOwnerStatusBox, RegisterTruckForm, PackagesForm, TruckName
from .models import EmailConfirmed, UserDefaultAddress, TruckOwnerStatus
from products.models import Product, ProductImage, Variation, VariationManager
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
# Create your views here.


def logout_view(request):
	print "logging out"
	logout(request)
	messages.success(request, "<strong>Successfully Logged out</strong>. Feel free to <a href='%s'>login</a> again." %(reverse("auth_login")), extra_tags='safe, abc')
	# messages.warning(request, "There's a warning.")
	# messages.error(request, "There's an error.")
	return HttpResponseRedirect('%s'%(reverse("auth_login")))

def login_view(request):
	form = LoginForm(request.POST or None)
	btn = "Login"
	form_title = "Login"
	caption = "Welcome Back"
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, "Successfully Logged In. Welcome Back!")
		return HttpResponseRedirect("/")
	context = {
		"form": form,
		"submit_btn": btn,
		"form_title": form_title,
		"caption": caption,
	}
	return render(request, "form.html", context)
	

def registration_view(request):
	form = RegistrationForm(request.POST or None)
	foodtruck_form = TruckOwnerStatusBox(request.POST or None)
	foodtruck_name = TruckName(request.POST or None)
	btn = "Join"
	form_title = "Registration Form"
	caption = "Awesome to have you onboard"
	if form.is_valid():
		# new_user = form.save(commit=False)
		# new_user.save()
		# new_foodtruck = foodtruck_form.save(commit=False)
	
		# new_foodtruck.save()
		# new_user.first_name = "Justin" this is where you can do stuff with the model form
		user = form.save()
		user.save()
		new_foodtruck = foodtruck_form.save(commit=False)
		new_foodtruck.user = user
		new_foodtruck.save()
		messages.success(request, "Successfully Registered. Please confirm your email now.")
		return HttpResponseRedirect("/")
	
		# username = form.cleaned_data['username']
		# password = form.cleaned_data['password']
		# user = authenticate(username=username, password=password)
		# login(request, user)
	# else:
	# 	messages.error(request, "Something's wrong")
	
	context = {
		 "form_title": form_title,
		 "form": form,
		 "foodtruck_form": foodtruck_form,
		 "submit_btn": btn,
		 "foodtruck_name": foodtruck_name,
		 "caption": caption,
	}
	return render(request, "form.html", context)


SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		print "activation key is real"
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			messages.success(request, "There was an error with your request.")
			return HttpResponseRedirect("/")
		if instance is not None and not instance.confirmed:
			page_message = "Your Confirmation Was Successful! Welcome to"
			instance.confirmed = True
			instance.activation_key = "Confirmed"
			instance.save()
			messages.success(request, "Successfully Confirmed! Please login.")
		elif instance is not None and instance.confirmed:
			page_message = "Already Confirmed"
			messages.success(request, "Already Confirmed.")
		else:
			page_message = ""

		context = {"page_message": page_message}
		return render(request, "accounts/activation_complete.html", context)
	else:
		raise Http404




def add_address(request):
	try:
		next_page = request.GET.get("next")
	except:
		next_page = None
	form = UserAddressForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			new_address = form.save(commit=False)
			new_address.user = request.user
			new_address.save()
			is_default = form.cleaned_data["default"]
			if is_default:
				default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
				default_address.shipping = new_address
				default_address.save()
				return HttpResponseRedirect(reverse('checkout'))
			if next_page is not None:
				return HttpResponseRedirect(reverse(str(next_page)))
	
	submit_btn = "Save Details"
	form_title = "Add New Address"
	return render(request, "accounts/add_address.html", 
		{"form": form,
		"submit_btn": submit_btn,
		"form_title": form_title,
		})	



@login_required
def profile(request):
	owner = TruckOwnerStatus.objects.get(user=request.user)
	try:
		trucks = Product.objects.filter(user=request.user)
	except ObjectDoesNotExist:
		pass
	
	context = {"trucks": trucks}
	template = 'accounts/profile.html'
	return render(request, template, context)



@login_required
def profile_add(request):
	user = request.user
	if request.method == 'GET':
		truck_form = RegisterTruckForm()
		context = {
			'truck_form': truck_form
		}
		return render(request, 'accounts/profile_add.html', context)

	elif request.method == 'POST':
		truck_form = RegisterTruckForm(request.POST, request.FILES)
		context = {
			'truck_form': truck_form
			}
		if truck_form.is_valid():
			truck = truck_form.save(commit=False)
			profile = Product.objects.create(user=request.user, owner_name=truck.owner_name, email=truck.email,\
				contact_number=truck.contact_number, foodtruck_name=truck.foodtruck_name, logo=truck.logo,\
				slogan=truck.slogan, about_us=truck.about_us, operating_state=truck.operating_state, bsb=truck.bsb,\
				account_number=truck.account_number, availability_link=truck.availability_link, slug=truck.slug)
			profile.save()
			# truck_form.save_m2m()
			# truck.save()
			context = {
			'truck_form': truck_form
			}
			messages.success(request, "Awesome. Your food truck profile has been successfully added. To get your page \
				up and running, let's <a href='%s'>add a package</a> next!" %(reverse("packages")), extra_tags='safe, abc')
			return HttpResponseRedirect(reverse("profile"))
		else:
			messages.error(request, "Below fields are required.")
	return render(request, 'accounts/profile_add.html', context)	



@login_required
def profile_edit(request):
	user = request.user
	truck = Product.objects.get(user=user)
	truck_form = RegisterTruckForm(instance=truck)

	if request.method == 'GET':
		context = {
			'truck_form': truck_form
		}

		return render(request, 'accounts/profile_edit.html', context)	

	elif request.method == 'POST':

		truck_form = RegisterTruckForm(request.POST, request.FILES, instance=truck)

		if truck_form.is_valid():
			truck = truck_form.save(commit=False)
			truck.product = Product.objects.get(user=request.user)

			truck_form.save_m2m()
			truck.save()
			context = {'truck_form': truck_form}
			messages.success(request, "Successfully Saved Edited!!")
			return HttpResponseRedirect(reverse("profile"))
		return render(request, 'accounts/profile_edit.html', context)


@login_required
def packages(request):
	truck_name = Product.objects.get(user=request.user)
	packages = Variation.objects.filter(product=truck_name)
	owner_name = Product.objects.get(user=request.user)
	print packages

	context = {"truck_name": truck_name, "packages": packages, "owner_name": owner_name}
	template = 'accounts/packages_index.html'
	return render(request, template, context)


@login_required
def packages_edit(request, variation_id):
	package = get_object_or_404(Variation, pk=variation_id)
	truck_name = Product.objects.get(user=request.user)
	if request.method == 'GET':
		packages_form = PackagesForm(instance=package)
		print "hello1"

		context = {
			'vid': variation_id,
			'packages_form': packages_form,
			'package': package,
		}
		return render(request, 'accounts/packages_edit.html', context)

	elif request.method == 'POST':
		packages_form = PackagesForm(request.POST, instance=package)

		if packages_form.is_valid():# and image_formset.is_valid():
			package = packages_form.save(commit=False)
			
			truck_name.package = Variation.objects.get(pk=variation_id)
			packages_form.save_m2m()
			package.save()

			# truck = truck_form.save(commit=False)
			# truck.product = Product.objects.get(user=request.user)
			# truck_form.save_m2m()
			# truck.save()

			messages.success(request, "Successfully Saved!!")
			return HttpResponseRedirect('/packages')
		else:

			messages.error(request, "All fields are required. If not applicable please enter a zero - 0")
	context = {"packages_form": packages_form}
	return render(request, 'accounts/packages_edit.html', context)




@login_required
def packages_add(request):
	owner = TruckOwnerStatus.objects.get(user=request.user)
	packages_form = PackagesForm()
	truck_name = Product.objects.get(user=request.user)
	if request.method == 'POST':
		print "1"	
		packages_form = PackagesForm(request.POST, request.FILES)	
		truck_owner = request.user
		# v = truck_owner.Variation.object.get_all()
		# print v
		# if packages_form.is_valid():
		# 	print "2"
			# new_package = packages_form.save(commit=False)
			# new_package.truck_name = Variation.objects.create(product=request.user.product)
			# packages_form.save_m2m()
			# new_package.save()

			# truck_name = packages_form.save(commit=False)
			# truck_name.package = Variation.objects.create()
			# packages_form.save()
			# truck_name.save()
			# print "3"
		if packages_form.is_valid():# and image_formset.is_valid():

			package = packages_form.save(commit=False)
			print package.menu
			truck_name = Product.objects.get(user=request.user)
			packages = Variation.objects.create(product=truck_name, title=package.title,\
												 price_per_guest=package.price_per_guest, minimum_guests=package.minimum_guests,\
												  maximum_guests=package.maximum_guests, included_travel_distance=package.included_travel_distance,\
												  included_service_hours=package.included_service_hours, extra_km_charge=package.extra_km_charge,\
												  extra_hours_charge=package.extra_hours_charge, \
												  gluten_free_options_upon_request=package.gluten_free_options_upon_request, menu=package.menu,\
												  vegetarian_options_upon_request=package.vegetarian_options_upon_request
												  )
			packages.save()
			print package.menu
			return HttpResponseRedirect('/packages')



			# package = packages_form.save(commit=False)
			# print package
			# package.save(user=request.user)

			# package.truck = Variation.objects.create()
	
			# package.truck.save()
	

			# truck_owner = packages_form.save(commit=False)
			# truck_owner.package = Variation.objects.get_or_create(product=truck_name, title='abc')
			# packages_form.save_m2m()
			# truck_owner.save()
			messages.success(request, "Successfully Saved!!")
			return HttpResponseRedirect('/')
		else:
			messages.error(request, "All fields are required. If not applicable please enter a zero - 0")
				
			# return render(request, context, 'accounts/profile_edit.html',)
	context = {"packages_form": packages_form}
	return render(request, 'accounts/packages_add.html', context)

	# truck_name = Product.objects.get(user=request.user)
	

	# context = {"packages_form": packages_form}
	# template = 'accounts/packages_add.html'



@login_required
def packages_delete(request, variation_id):
	package = get_object_or_404(Variation, id=variation_id)
	package.delete()
	return HttpResponseRedirect('/packages')


@login_required
def support(request):
	user = request.user
	foodtrucks = Product.objects.filter(user=user)
	for i in foodtrucks:
		foodtruck = i
	context = {"foodtruck": foodtruck}
	return render(request, 'accounts/support.html', context)



def custom_404(request):
    return render(request, '404.html', context)


def custom_500(request):
    return render(request, '500.html', context)