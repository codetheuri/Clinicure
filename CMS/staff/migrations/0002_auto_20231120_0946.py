# Generated by Django 3.2.21 on 2023-11-20 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffs',
            name='address',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='phone_number',
        ),
    ]