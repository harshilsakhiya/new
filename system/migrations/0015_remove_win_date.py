# Generated by Django 4.2.4 on 2024-04-30 15:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0014_rename_eighty_win_eight_rename_fifteen_win_fifty_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="win",
            name="date",
        ),
    ]
