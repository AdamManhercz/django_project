# Generated by Django 4.1.6 on 2023-02-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("food_planner", "0013_delete_recipelist"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipeList",
            fields=[
                (
                    "recipes",
                    models.CharField(
                        max_length=250, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("urls", models.URLField(unique=True)),
                ("images", models.URLField(unique=True, verbose_name=300)),
            ],
        ),
    ]