from attribute.models import Attribute, AttributeName, AttributeValue,ProductAttributes
from product.models import Product, Catalog, Image, ProductImage
from rest_framework import serializers


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


