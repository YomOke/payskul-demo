# Generated by Django 4.1.3 on 2022-12-17 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_profile_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="dob",
            field=models.DateField(),
        ),
    ]