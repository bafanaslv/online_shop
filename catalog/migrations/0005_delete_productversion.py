# Generated by Django 5.0.6 on 2024-07-11 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_productversion_alter_products_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductVersion',
        ),
    ]
