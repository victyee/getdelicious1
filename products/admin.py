from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Variation, Category

class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp' #updated
	search_fields = ['foodtruck_name', 'description']
	list_display = ['foodtruck_name', 'active', 'updated']
	list_editable = ['active']
	list_filter = ['active']
	readonly_fields = ['updated', 'timestamp']
	# prepopulated_fields = {"slug": ("foodtruck_name",)}
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)


admin.site.register(ProductImage)
admin.site.register(Variation)
admin.site.register(Category)