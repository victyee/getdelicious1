from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

from products.models import Product, Variation

from .models import Cart, CartItem

def view(request):
	user = request.user
	print user
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None		
	if the_id:
		new_total = 0.00
		for item in cart.cartitem_set.all():
			pass
			for variation in item.variations.all():
				line_total = (float(variation.price_per_guest) * item.quantity) + (float(variation.extra_km_charge) * item.distance) + (float(variation.extra_hours_charge) * item.hour)
				new_total += line_total
				# subtotal_guests = variation.price_per_guest * item.quantity
				# subtotal_km_charges = variation.extra_km_charge * item.distance
				# subtotal_hours_charges = variation.extra_hours_charge * item.hour
		request.session['items_total'] = cart.cartitem_set.count()
		cart.total = new_total
		cart.save()
		context = { "cart": cart,
					"user": user,
					# "subtotal_guests": subtotal_guests,
					# "subtotal_km_charges": subtotal_km_charges,
					# "subtotal_hours_charges": subtotal_hours_charges,
					}
	else:
		empty_message = "You've not made any bookings yet. Let's get started!"
		context = {"empty": True, "empty_message": empty_message, "user": user}
	
	template = "cart/view.html"
	return render(request, template, context)


def remove_from_cart(request, id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("cart"))

	cartitem = CartItem.objects.get(id=id)
	#cartitem.delete()
	cartitem.cart = None
	cartitem.save()
	#send "success message"
	return HttpResponseRedirect(reverse("cart"))
		



def add_to_cart(request, slug):
	request.session.set_expiry(120000)

	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id
	
	cart = Cart.objects.get(id=the_id)

	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	product_var = [] #product variation
	if request.method == "POST":
		qty = request.POST['qty']
		distance = request.POST['distance']
		hour = request.POST['hour']
		for item in request.POST:
			key = item
			val = request.POST[key]
			try:
				v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
				product_var.append(v)
			except:
				pass

		total = float(qty) + float(v.minimum_guests)
		if float(qty) > float(v.maximum_guests):
			messages.error(request, "Unfortunately <strong>%s</strong> guests has exceeded <strong>%s</strong>'s maximum capacity of <strong>%s</strong> guests. \
				Please reduce the number of guests." % (qty, v, v.maximum_guests), extra_tags='safe, abc')

		elif float(qty) >= float(v.minimum_guests):
			cart_item = CartItem.objects.create(cart=cart, product=product)
			if len(product_var) > 0:
				cart_item.variations.add(*product_var)
			cart_item.quantity = qty
			cart_item.distance = distance
			cart_item.hour = hour
			cart_item.save()
			# success message
			return HttpResponseRedirect(reverse("cart"))

		else:
			messages.error(request, "<strong>%s</strong> requires a minimum of <strong>%s</strong> guests. \
				Please increase the number of guests." % (v, v.minimum_guests), extra_tags='safe, abc')
	#error message
	return HttpResponseRedirect(reverse("cart"))