# Generated by Django 4.1.3 on 2022-11-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cena',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
