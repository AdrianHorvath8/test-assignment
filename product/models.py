from django.db import models

class Project(models.Model):
    nazev = models.CharField(max_length=150,null=True, blank=True )
    description = models.TextField(max_field = 500, null=True, blank=True)
    cena = models.CharField(max_length=150,null=True, blank=True )
    mena = models.CharField(max_length=50,null=True, blank=True )
    published_on = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
