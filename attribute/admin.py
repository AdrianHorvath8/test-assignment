from django.contrib import admin
from .models import ProductAttributes, Attribute, AttributeName, AttributeValue

admin.site.register(ProductAttributes)
admin.site.register(Attribute)
admin.site.register(AttributeName)
admin.site.register(AttributeValue)