from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from localflavor.au.au_states import STATE_CHOICES
# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	featured = models.BooleanField(default=None)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return self.title

# T-Shirt 1
# Active Wear 2
# Women's Clothing 3


class Product(models.Model):
	user = models.OneToOneField(User)
	owner_name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	contact_number = models.CharField(max_length=15, null=True, blank=True)
	foodtruck_name = models.CharField(max_length=120)
	logo = models.ImageField(upload_to='foodtruck/logo/', null=True, blank=True)
	slogan = models.TextField(max_length=60, null=True, blank=True)
	about_us = models.TextField(max_length=150, null=True, blank=True)
	operating_state = models.CharField(max_length=120, choices=STATE_CHOICES)
	bsb = models.IntegerField(max_length=15, null=True, blank=True)
	account_number = models.IntegerField(max_length=15, null=True, blank=True)
	availability_link = models.CharField(max_length=300, null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)

	#OLD FIELDS
	# price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	# category = models.ManyToManyField(Category, null=True, blank=True)
	# title = models.CharField(max_length=120)
	# sale_price = models.DecimalField(decimal_places=2, max_digits=100,null=True, blank=True)
												

	def __unicode__(self):
		return self.foodtruck_name

	# class Meta:
	# 	unique_together = ('foodtruck_name', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.product.foodtruck_name




class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)#only shows variance if it is active

	def packages(self):
		return self.all().filter(category='package')


VAR_CATEGORIES = (
	('package', 'package'),
)


class Variation(models.Model):
	product = models.ForeignKey(Product)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='package')
	title = models.CharField(max_length=120)
	# image = models.ImageField(upload_to='foodtruck/packages/')
	price_per_guest = models.DecimalField(max_digits=1000, decimal_places=2)
	minimum_guests = models.DecimalField(max_digits=1000, decimal_places=2)
	maximum_guests = models.DecimalField(max_digits=1000, decimal_places=2)
	included_travel_distance = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
	included_service_hours = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
	extra_km_charge = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
	extra_hours_charge = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
	gluten_free_options_upon_request = models.NullBooleanField(default=False)
	vegetarian_options_upon_request= models.NullBooleanField(default=False)
	menu = models.TextField(max_length=50000)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)



	objects = VariationManager()

	def __unicode__(self):
		return self.title


def product_defaults(sender, instance, created, *args, **kwargs):
	if instance.update_defaults:
		categories = instance.category.all()
		print categories
		for cat in categories:
			print cat.id
			if cat.id == 1: #for t-shirts
				small_size = Variation.objects.get_or_create(product=instance, 
											category='size', 
											title='Small')
				medium_size = Variation.objects.get_or_create(product=instance, 
											category='size', 
											title='Medium')
				large_size = Variation.objects.get_or_create(product=instance, 
											category='size', 
											title='Large')
		instance.update_defaults = False
		instance.save()
	#print args, kwargs

post_save.connect(product_defaults, sender=Product)
