# Generated by Django 2.1 on 2018-10-05 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_wishlisttreeitem_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistproductitem',
            name='qty',
        ),
    ]
