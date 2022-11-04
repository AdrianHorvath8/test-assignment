from django.contrib import admin
from .models import Product, Catalog, Image, ProductImage

admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(Image)
admin.site.register(ProductImage)