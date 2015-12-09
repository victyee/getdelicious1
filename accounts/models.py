

from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from localflavor.au.au_states import STATE_CHOICES
# Create your models here.


# NEW_STATE = (
# 	('AB', "ABC STATE"),
# 	('BC', "BC STATE"),
# 	)


class UserDefaultAddress(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	shipping = models.ForeignKey("UserAddress", null=True,\
					 blank=True, related_name="user_address_shipping_default")
	# billing = models.ForeignKey("UserAddress", null=True,\
	# 				blank=True, related_name="user_address_billing_default")

	def __unicode__(self):
		return str(self.user.username)



# class UserAddressManager(models.Manager):
# 	def get_billing_addresses(self, user):
# 		return super(UserAddressManager, self).filter(billing=True).filter(user=user)

class UserAddress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True)
	contact_person_name = models.CharField(max_length=100)
	phone =  models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	date = models.CharField(max_length=30)
	time_from = models.CharField(max_length=20)
	time_to = models.CharField(max_length=20)
	address = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=120, choices=STATE_CHOICES)
	postcode = models.CharField(max_length=25)
	shipping = models.BooleanField(default=True)
	billing = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	message = models.TextField(max_length=500, null=True, blank=True)

	def __unicode__(self):
		return self.get_address()

	def get_address(self):
		return "ADD: %s, %s, %s, %s, %s NAME: %s PHONE: %s EMAIL: %s DATE: %s START: %s END: %s MSG: %s" %(self.address, self.address2, self.city, self.state, self.postcode,\
		self.contact_person_name, self.phone, self.email, self.date, self.time_from, self.time_to, self.message)

	# objects = UserAddressManager()

	class Meta:
		ordering = ['-updated', '-timestamp']


class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return str(self.stripe_id)

#cus_4iMQyUSLNMrCxe
####cus_4iMT2JwLrE8sWx


class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.confirmed)

	def activate_user_email(self):
		#send email here & render a string
		activation_url = "%s%s" %(settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
		context = {
			"activation_key": self.activation_key,
			"activation_url": activation_url,
			"user": self.user.username,
		}
		message = render_to_string("accounts/activation_message.txt", context)
		subject = "Activate your Email"
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.user.email], kwargs)




class EmailMarketingSignUp(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	#confirmed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.email)



class TruckOwnerStatus(models.Model):
    user = models.OneToOneField(User)
    foodtruck_owner = models.BooleanField(default=False)
 
    def __unicode__(self):
        return self.user.username




	



