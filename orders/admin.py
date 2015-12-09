from django.contrib import admin

# Register your models here.

from .models import Order


class OrderAdmin(admin.ModelAdmin):

	list_display = ['user', 'status', 'updated', 'shipping_address', 'final_total']

	# prepopulated_fields = {"slug": ("foodtruck_name",)}
	class Meta:
		model = Order


admin.site.register(Order, OrderAdmin)