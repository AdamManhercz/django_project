# Generated by Django 4.1.6 on 2023-02-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_planner", "0009_alter_recipelist_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipelist",
            name="images",
            field=models.URLField(unique=True, verbose_name=300),
        ),
    ]