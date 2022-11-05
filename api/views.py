from django.shortcuts import render
from rest_framework.decorators import api_view
from attribute.models import Attribute, AttributeName, AttributeValue,ProductAttributes
from product.models import Product, Catalog, Image, ProductImage
from rest_framework.response import Response
from .serializers import (
    AttributeSerializer, AttributeNameSerializer, AttributeValueSerializer,
    ProductAttributesSerializer, ProductSerializer, ProductImageSerializer,
    ImageSerializer, CatalogSerializer
    )
from rest_framework import status
import json


@api_view(['GET'])
def get_routes(request):
    routes = [
        {"POST":"/api/import"},

        {"GET":"/api/detail/attributes"},
        {"GET":"/api/detail/attributes/id"},

        {"GET":"/api/detail/attribute_names"},
        {"GET":"/api/detail/attribute_names/id"},

        {"GET":"/api/detail/attribute_values"},
        {"GET":"/api/detail/attribute_values/id"},

        {"GET":"/api/detail/product_attributes"},
        {"GET":"/api/detail/product_attributes/id"},

        {"GET":"/api/detail/products"},
        {"GET":"/api/detail/products/id"},

        {"GET":"/api/detail/productimages"},
        {"GET":"/api/detail/productimages/id"},

        {"GET":"/api/detail/images"},
        {"GET":"/api/detail/images/id"},

        {"GET":"/api/detail/catalogs"},
        {"GET":"/api/detail/catalogs/id"},
    ]
    return Response(routes)
# tu sa nachadzaju všetky dostupne routes


@api_view(["POST"])
def import_data(request):
    
    with open('test_data.json', 'r', encoding="utf8") as data_file:
        data_array = json.load(data_file)
    # uložime data do data_array
    for model in data_array:

        for model_name in model:           
            # model_name je nazov modelu
            attribute_names_values = model[model_name]
            # attribute_names_values je stlpec a value stlpca
            # attribute_names_values["id"], viem pristupovať k value daneho stlpca

            if model_name == "Attribute":
                
                try:
                    item = Attribute.objects.create(
                        nazev_atributu_id = attribute_names_values["nazev_atributu_id"],
                        hodnota_atributu_id = attribute_names_values["hodnota_atributu_id"]
                    )
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            # ak nazov modelu je Attribute vytvor object v Attribute databaze a daj do neho nasledovne data

            if model_name == "AttributeName":
                
                try:
                    item = AttributeName.objects.create(
                        nazev = attribute_names_values["nazev"] if "nazev" in attribute_names_values else None,
                        kod = attribute_names_values["kod"] if "kod" in attribute_names_values else None,
                        zobrazit = attribute_names_values["zobrazit"] if "zobrazit" in attribute_names_values else False,
                        #ak sa kod nachadza v AttributeName napiš do stlpca kod value ak nie tak None/null
                    )
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            if model_name == "AttributeValue":
                
                try:
                    item = AttributeValue.objects.create(
                        hodnota = attribute_names_values["hodnota"],
                        
                    )
                    
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)


            if model_name == "ProductAttributes":
                
                try:
                    item = ProductAttributes.objects.create(
                        attribute = attribute_names_values["attribute"],
                        product = attribute_names_values["product"]
                    )
                    item.save()
                    
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)


            if model_name == "Product":
                                
                try:
                    if "nazev" in attribute_names_values:
                        item = Product.objects.create(
                            nazev = attribute_names_values["nazev"],
                            description = attribute_names_values["description"],
                            cena = float(attribute_names_values["cena"]),
                            mena = attribute_names_values["mena"],
                            published_on = attribute_names_values["published_on"] if "published_on" in attribute_names_values else None,
                            is_published = attribute_names_values["is_published"],
                        )
                        item.save()
                    else:
                        continue
                except:        
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            

            if model_name == "Catalog":
                             
                try:
                    if "nazev" in attribute_names_values:
                        item = Catalog.objects.create(
                            nazev = attribute_names_values["nazev"] if "nazev" in attribute_names_values else None,
                            obrazek_id = attribute_names_values["obrazek_id"] if "obrazek_id" in attribute_names_values else None,
                            products_ids = attribute_names_values["products_ids"],
                            attributes_ids = attribute_names_values["attributes_ids"] if "attributes_ids" in attribute_names_values else [],
                        )
                        item.save()
                    else:
                        continue
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                


            if model_name == "Image":
                
                try:
                    item = Image.objects.create(
                        nazev = attribute_names_values["nazev"] if "nazev" in attribute_names_values else None,
                        obrazek = attribute_names_values["obrazek"]
                    )
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)


            if model_name == "ProductImage":
                                
                try:
                    item = ProductImage.objects.create(
                        product = attribute_names_values["product"],
                        obrazek_id = attribute_names_values["obrazek_id"],
                        nazev = attribute_names_values["nazev"]
                    )
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)


    return Response(status=status.HTTP_200_OK)
# tu sa nachadza views pre import dat z json filu


@api_view(["GET"])
def all_data(request, model_name):
    if model_name == "attributes":
        attributes = Attribute.objects.all()
        serializer = AttributeSerializer(attributes, many = True)

    if model_name == "attribute_names":
        attribute_names = AttributeName.objects.all()
        serializer = AttributeNameSerializer(attribute_names, many = True)

    if model_name == "attribute_values":
        attribute_values = AttributeValue.objects.all()
        serializer = AttributeValueSerializer(attribute_values, many = True)
    
    if model_name == "product_attributes":
        product_attributes = ProductAttributes.objects.all()
        serializer = ProductAttributesSerializer(product_attributes, many = True)
    
    if model_name == "products":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
    
    if model_name == "productimages":
        productimages = ProductImage.objects.all()
        serializer = ProductImageSerializer(productimages, many = True)
    
    if model_name == "images":
        images = Image.objects.all()
        serializer = ImageSerializer(images, many = True)
    
    if model_name == "catalogs":
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many = True)

    try:
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

# tu sa nachadza views pre všetky data na zaklade nazvu modelu




@api_view(["GET"])
def data_by_id(request, pk, model_name):
    
    if model_name == "attributes":
        attributes = Attribute.objects.get(id=pk)
        serializer = AttributeSerializer(attributes, many = False)

    if model_name == "attribute_names":
        attribute_names = AttributeName.objects.get(id=pk)
        serializer = AttributeNameSerializer(attribute_names, many = False)

    if model_name == "attribute_values":
        attribute_values = AttributeValue.objects.get(id=pk)
        serializer = AttributeValueSerializer(attribute_values, many = False)
    
    if model_name == "product_attributes":
        product_attributes = ProductAttributes.objects.get(id=pk)
        serializer = ProductAttributesSerializer(product_attributes, many = False)
    
    if model_name == "products":
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products, many = False)
    
    if model_name == "productimages":
        productimages = ProductImage.objects.get(id=pk)
        serializer = ProductImageSerializer(productimages, many = False)
    
    if model_name == "images":
        images = Image.objects.get(id=pk)
        serializer = ImageSerializer(images, many = False)
    
    if model_name == "catalogs":
        catalogs = Catalog.objects.get(id=pk)
        serializer = CatalogSerializer(catalogs, many = False)

    try:
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

# tu sa nachadza views predata na zaklade nazvu modelu a ID