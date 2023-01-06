import os

from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField


def upload_picture(instance, orig_filename):
    _filename, ext = os.path.splitext(orig_filename)
    return f"{slugify(instance.recipe_name)}{ext}"


class RecipeIngredient(models.Model):
    class Meta:
        ordering = ["ingredient"]

    ingredient = models.CharField(max_length=40)

    def __str__(self):
        return self.ingredient.capitalize()

    '''class Meta:
        ordering = ['ingredient']'''


class RecipeUnit(models.Model):
    recipe_unit = models.CharField(max_length=10, null=True, blank=True)
    recipe_unit_name = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.recipe_unit + ' (' + self.recipe_unit_name + ')'


class RecipeClass(models.Model):
    class_name = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from="class_name")
    recipe_count = models.IntegerField(default=0)
    class_visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.class_name


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
    recipe_ingredient = models.ForeignKey(RecipeIngredient, on_delete=models.CASCADE, related_name="recipe_tables")
    recipe_ingredient_amount = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    recipe_ingredient_unit = models.ForeignKey(RecipeUnit, blank=True, null=True, on_delete=models.CASCADE,
                                               related_name="recipe_tables")

    def __str__(self):
        return self.recipe.recipe_name

    '''class Meta:
        ordering = ['recipe_ingredient']'''


@receiver(models.signals.pre_save, sender=RecipeTable)
def recipetable_presave(sender, instance, *args, **kwargs):
    # delete all recipetable entries for current recipe, so they wont show up as double entries
    # RecipeTable.objects.filter(recipe_id=instance.recipe_id).delete()
    pass


@receiver(models.signals.pre_save, sender=Recipe)
def execute_before_save(sender, instance, *args, **kwargs):
    pass


@receiver(models.signals.post_save, sender=Recipe)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        recipe_class = RecipeClass.objects.get(id=instance.recipe_class.id)
        recipe_class.recipe_count = Recipe.objects.filter(recipe_class=instance.recipe_class.id).count()
        recipe_class.save()
