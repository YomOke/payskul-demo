# Generated by Django 4.1.3 on 2022-12-18 14:11

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_alter_profile_dob"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="userauthcodes",
            managers=[
                ("expired", django.db.models.manager.Manager()),
            ],
        ),
    ]
