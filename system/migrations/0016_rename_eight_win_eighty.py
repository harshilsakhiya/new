# Generated by Django 4.2.4 on 2024-04-30 15:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0015_remove_win_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="win",
            old_name="eight",
            new_name="eighty",
        ),
    ]