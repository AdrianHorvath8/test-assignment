# Generated by Django 4.1.3 on 2022-11-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributename',
            name='zobraziť',
            field=models.BooleanField(default=False),
        ),
    ]
