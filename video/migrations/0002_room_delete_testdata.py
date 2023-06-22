# Generated by Django 4.2.1 on 2023-05-05 12:37

import shortuuidfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("roomId", shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
            ],
        ),
        migrations.DeleteModel(
            name="TestData",
        ),
    ]
