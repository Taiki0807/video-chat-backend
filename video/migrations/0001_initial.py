# Generated by Django 4.2.1 on 2023-05-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestData",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("testname", models.CharField(max_length=100)),
                ("testvalue", models.IntegerField()),
            ],
        ),
    ]
