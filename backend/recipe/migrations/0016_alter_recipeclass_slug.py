# Generated by Django 4.1.5 on 2023-02-07 14:05

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_rename_recipeunit_ingredientunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeclass',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]