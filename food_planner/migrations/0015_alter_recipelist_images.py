# Generated by Django 4.1.6 on 2023-02-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_planner", "0014_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipelist",
            name="images",
            field=models.URLField(verbose_name=300),
        ),
    ]