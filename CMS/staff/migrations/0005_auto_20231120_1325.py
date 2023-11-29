# Generated by Django 3.2.21 on 2023-11-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_staffs_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffs',
            name='department',
        ),
        migrations.AlterField(
            model_name='staffs',
            name='position',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse'), ('receptionist', 'Administrator'), ('pharmacy', 'Pharmacist')], default='doctor', max_length=20),
        ),
    ]
