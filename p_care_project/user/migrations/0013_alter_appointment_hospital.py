# Generated by Django 5.0.4 on 2024-06-26 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('user', '0012_petprofile_pet_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.hospital'),
        ),
    ]