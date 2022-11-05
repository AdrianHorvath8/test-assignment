from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    nazev = models.CharField(max_length=150,null=True, blank=True )
    description = models.TextField(max_length = 500, null=True, blank=True)
    cena = models.FloatField(blank=True, null=True)
    mena = models.CharField(max_length=50,null=True, blank=True )
    published_on = models.CharField(max_length=200,null=True, blank=True )
    is_published = models.BooleanField(default=True)


class ProductImage(models.Model):
    product = models.IntegerField(blank=True, null=True)
    obrazek_id = models.IntegerField(blank=True, null=True)
    nazev = models.CharField(max_length=150,null=True, blank=True )


class Image(models.Model):
    nazev = models.CharField(max_length=150,null=True, blank=True )
    obrazek = models.CharField(max_length=300,null=True, blank=True )


class Catalog(models.Model):
    nazev = models.CharField(max_length=150,null=True, blank=True )
    obrazek_id = models.IntegerField(blank=True, null=True)
    attributes_ids = ArrayField(models.IntegerField())
    products_ids = ArrayField(models.IntegerField())