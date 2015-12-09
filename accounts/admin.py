from django.contrib import admin

# Register your models here.
from .models import UserStripe, EmailConfirmed, EmailMarketingSignUp, UserAddress, UserDefaultAddress

from .models import TruckOwnerStatus

class UserAddressAdmin(admin.ModelAdmin):
	class Meta:
		model = UserAddress

admin.site.register(UserAddress, UserAddressAdmin)


admin.site.register(UserDefaultAddress)


admin.site.register(UserStripe)

admin.site.register(EmailConfirmed)


class EmailMarketingSignUpAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']
	class Meta:
		model = EmailMarketingSignUp


admin.site.register(EmailMarketingSignUp, EmailMarketingSignUpAdmin)


admin.site.register(TruckOwnerStatus)