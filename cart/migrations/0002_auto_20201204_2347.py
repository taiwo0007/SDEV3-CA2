# Generated by Django 3.1.3 on 2020-12-04 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quantitiy',
            new_name='quantity',
        ),
    ]
