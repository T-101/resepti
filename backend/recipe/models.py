import os
from io import BytesIO

from django.db import models
from django.utils.text import slugify
from django.core.files.base import ContentFile

from django_extensions.db.fields import AutoSlugField
from PIL import Image


def upload_picture(instance, orig_filename):
    _filename, ext = os.path.splitext(orig_filename)
    return f"{slugify(instance.name)}{ext}"


class Ingredient(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return self.name.capitalize()


class IngredientUnit(models.Model):
    unit = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.unit + ' (' + self.name + ')'


class RecipeClass(models.Model):
    class Meta:
        verbose_name_plural = "Recipe classes"

    name = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from="name")
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name")
    recipe_class = models.ForeignKey(RecipeClass, on_delete=models.CASCADE, related_name="recipies")
    instructions = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to=upload_picture, blank=True)
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.picture:
            img = Image.open(self.picture)
            # Convert the image to WebP format
            if img.format != 'WEBP':
                buffer = BytesIO()
                img.save(buffer, format='WEBP')
                self.picture.save(
                    f"{self.picture.name.split('.')[0]}.webp",
                    ContentFile(buffer.getvalue()),
                    save=False
                )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeTable(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_tables")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe_tables")
    ingredient_amount = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    ingredient_unit = models.ForeignKey(IngredientUnit, blank=True, null=True, on_delete=models.CASCADE,
                                        related_name="recipe_tables")

    def __str__(self):
        return self.recipe.name
