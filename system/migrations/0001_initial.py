# Generated by Django 4.2.4 on 2024-04-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("Address", models.CharField(max_length=30)),
                ("Email", models.CharField(max_length=12)),
                ("phone", models.CharField(max_length=12)),
            ],
        ),
    ]
