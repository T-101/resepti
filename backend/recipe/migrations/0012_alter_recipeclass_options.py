# Generated by Django 4.1.5 on 2023-01-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_rename_class_visibility_recipeclass_is_visible_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeclass',
            options={'verbose_name_plural': 'Recipe classes'},
        ),
    ]
