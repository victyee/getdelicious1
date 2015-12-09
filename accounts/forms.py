from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from products.models import Product, Variation
from .models import TruckOwnerStatus


User = get_user_model()

from .models import UserAddress


class UserAddressForm(forms.ModelForm):
	default = forms.BooleanField(label='I confirm all details are correct.')
	class Meta:
		model = UserAddress
		fields = ["contact_person_name",
				"phone",
				"email",
				"date",
				"time_from",
				"time_to",
				"address", 
				"address2", 
				"city", 
				"state", 
				"postcode", 
				"message",
				]



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError("Invalid Password")
		elif user is None:
			pass
		else:
			return password


class RegistrationForm(forms.ModelForm):
	email = forms.EmailField(label='Your Email')
	password1 = forms.CharField(label='Password', \
					widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password Confirmation', \
					widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email']


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2

	def clean_email(self):
		email = self.cleaned_data.get("email")
		user_count = User.objects.filter(email=email).count()
		if user_count > 0:
			raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
		return email


	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1']) 
		if commit:
			user.save()
		return user


class TruckOwnerStatusBox(forms.ModelForm):
	class Meta:
		model = TruckOwnerStatus
		fields = ['foodtruck_owner']



class RegisterTruckForm(forms.ModelForm):

	class Meta:
		model = Product
		include = ('owner_name', 'email', 'contact_number', 'foodtruck_name', 'logo', 'slogan', 'about_us'\
					'operating_state', 'bsb', 'account_number', 'slug')
		exclude = ('user', 'availability_link', 'active', 'update_defaults',)



class PackagesForm(forms.ModelForm):

	class Meta:
		model = Variation
		include = ('title', 'price_per_guest', 'minimum_guests', 'maximum_guests', 'included_travel_distance',\
				 'included_service_hours', 'menu', 'extra_km_charge', 'extra_hours_charge', 'gluten_free_options_upon_request', \
				 'vegetarian_options_upon_request', 'active',)
		exclude = ('product', 'category',)


class TruckName(forms.ModelForm):

	class Meta:
		model = Product
		exclude = ('user', 'email', 'owner_name', 'contact_number', 'logo', 'slogan', 'about_us', 'operating_state', 'bsb', 'account_number', 'availability_link', 'slug', 'active', 'update_defaults', 'timestamp', 'updated',)


