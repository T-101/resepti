# Generated by Django 4.1.5 on 2023-01-07 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_alter_recipeclass_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_instructions',
            new_name='instructions',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_visibility',
            new_name='is_visible',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_picture',
            new_name='picture',
        ),
    ]
