from django.shortcuts import render
from rest_framework.decorators import api_view
from attribute.models import Attribute, AttributeName, AttributeValue,ProductAttributes
from product.models import Product, Catalog, Image, ProductImage
from rest_framework.response import Response
from .serializers import AttributeSerializer
from rest_framework import status
import json


@api_view(['GET'])
def get_routes(request):
    routes = [
        {"POST":"/api/import"},

        {"GET":"/api/detail/attributes"},
        {"GET":"/api/detail/attributes/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},

        {"GET":"/api/detail"},
        {"GET":"/api/detail/id"},
    ]
    return Response(routes)


@api_view(["POST"])
def import_data(request):
    
    with open('test_data.json', 'r', encoding="utf8") as data_file:
        data_array = json.load(data_file)

    for model in data_array:

        for model_name in model:           
            # model_name je nazov modelu
            # attribute_names_values je stlpec a value stlpca
            # attribute_names_values["id"], viem pristupovať k value daneho stlpca
            print("i")
            
            attribute_names_values = model[model_name]


            if model_name == "Attribute":
                try:
                    item = Attribute.objects.create(
                        nazev_atributu_id = attribute_names_values["nazev_atributu_id"],
                        hodnota_atributu_id = attribute_names_values["hodnota_atributu_id"]
                    )
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)


            if model_name == "AttributeName":
                item = AttributeName.objects.create(
                    nazev = attribute_names_values["nazev"] if "nazev" in attribute_names_values else None,
                    kod = attribute_names_values["kod"] if "kod" in attribute_names_values else None,
                    zobrazit = attribute_names_values["zobrazit"] if "zobrazit" in attribute_names_values else False,
                    #ak sa kod nachadza v zobrazit tak zapiš zobrazit ak nie empty str
                )
                item.save()

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
                    item = Attribute.objects.create(
                        nazev = attribute_names_values["nazev"],
                        description = attribute_names_values["description"],
                        cena = attribute_names_values["cena"],
                        mena = attribute_names_values["mena"],
                        published_on = attribute_names_values["published_on"]if "published_on" in attribute_names_values else None,
                        is_published = attribute_names_values["is_published"],
                    )
                    item.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            if model_name == "Catalog":
                try:
                    item = Catalog.objects.create(
                        nazev = attribute_names_values["nazev"] if "nazev" in attribute_names_values else None,
                        obrazek_id = attribute_names_values["obrazek_id"] if "obrazek_id" in attribute_names_values else None,
                        products_ids = attribute_names_values["products_ids"],
                        attributes_ids = attribute_names_values["attributes_ids"] if "attributes_ids" in attribute_names_values else None,
                    )
                    item.save()
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





@api_view(["GET"])
def attributes(request):

    attributes = Attribute.objects.all()
    serializer = AttributeSerializer(attributes, many = True)


    return Response(serializer.data)