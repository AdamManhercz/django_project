# Generated by Django 4.1.6 on 2023-02-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_planner", "0026_alter_recipelist_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipelist",
            name="images",
            field=models.CharField(max_length=350, unique=True),
        ),
    ]
