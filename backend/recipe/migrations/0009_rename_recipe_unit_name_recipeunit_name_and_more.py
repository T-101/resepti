# Generated by Django 4.1.5 on 2023-01-07 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_alter_recipeingredient_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeunit',
            old_name='recipe_unit_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='recipeunit',
            old_name='recipe_unit',
            new_name='unit',
        ),
    ]
