# Generated by Django 4.1.1 on 2022-09-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manageitems", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keyboard",
            name="has_back_light",
            field=models.BooleanField(null=True),
        ),
    ]