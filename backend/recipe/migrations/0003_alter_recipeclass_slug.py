# Generated by Django 4.1.5 on 2023-01-06 17:05

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipeclass_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeclass',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='class_name'),
        ),
    ]
