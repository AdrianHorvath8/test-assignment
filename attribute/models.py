from django.db import models

class Attribute(models.Model):
    nazev_atributu_id = models.IntegerField(blank=True, null=True)
    hodnota_atributu_id = models.IntegerField(blank=True, null=True)


class AttributeName(models.Model):
    nazev = models.CharField(max_length=150,null=True, blank=True )
    kod = models.CharField(max_length=150,null=True, blank=True )
    zobrazit = models.BooleanField(default = False)


class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=150,null=True, blank=True )


class ProductAttributes(models.Model):
    attribute = models.IntegerField(blank=True, null=True)
    product = models.IntegerField(blank=True, null=True)