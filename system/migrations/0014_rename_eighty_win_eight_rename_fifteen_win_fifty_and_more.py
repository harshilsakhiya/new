# Generated by Django 4.2.4 on 2024-04-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0013_win_total"),
    ]

    operations = [
        migrations.RenameField(
            model_name="win",
            old_name="eighty",
            new_name="eight",
        ),
        migrations.RenameField(
            model_name="win",
            old_name="fifteen",
            new_name="fifty",
        ),
        migrations.AddField(
            model_name="win",
            name="date",
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
