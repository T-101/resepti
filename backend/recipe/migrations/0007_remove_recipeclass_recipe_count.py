# Generated by Django 4.1.5 on 2023-01-07 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipe_recipe_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeclass',
            name='recipe_count',
        ),
    ]
