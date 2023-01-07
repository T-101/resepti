import os

from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField


def upload_picture(instance, orig_filename):
    _filename, ext = os.path.splitext(orig_filename)
    return f"{slugify(instance.recipe_name)}{ext}"


class RecipeIngredient(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name.capitalize()


class RecipeUnit(models.Model):
    unit = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.unit + ' (' + self.name + ')'


class RecipeClass(models.Model):
    class Meta:
        verbose_name_plural = "Recipe classes"
    name = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from="class_name")
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="recipe_name")
    recipe_class = models.ForeignKey(RecipeClass, on_delete=models.CASCADE, related_name="recipies")
    recipe_instructions = models.TextField(blank=True, null=True)
    recipe_picture = models.ImageField(upload_to=upload_picture, blank=True)
    recipe_visibility = models.BooleanField(default=True)

    def instructions_as_list(self):
        return self.recipe_instructions.split('\r\n\r\n')

    def __str__(self):
        return self.recipe_name


class RecipeTable(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_tables")
    ingredient = models.ForeignKey(RecipeIngredient, on_delete=models.CASCADE, related_name="recipe_tables")
    ingredient_amount = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    ingredient_unit = models.ForeignKey(RecipeUnit, blank=True, null=True, on_delete=models.CASCADE,
                                        related_name="recipe_tables")

    def __str__(self):
        return self.recipe.recipe_name
