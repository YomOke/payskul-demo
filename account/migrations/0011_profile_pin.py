# Generated by Django 4.1.3 on 2022-12-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0010_alter_profile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="pin",
            field=models.CharField(default="12345", max_length=15),
        ),
    ]
