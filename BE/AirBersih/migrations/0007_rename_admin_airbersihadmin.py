# Generated by Django 5.1.2 on 2024-12-06 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AirBersih', '0006_remove_sumberair_jenis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='AirBersihAdmin',
        ),
    ]
