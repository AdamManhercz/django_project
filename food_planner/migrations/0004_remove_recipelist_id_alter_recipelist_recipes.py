# Generated by Django 4.1.6 on 2023-02-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_planner", "0003_alter_recipelist_recipes_alter_recipelist_url_links"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipelist",
            name="id",
        ),
        migrations.AlterField(
            model_name="recipelist",
            name="recipes",
            field=models.CharField(
                max_length=250, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
