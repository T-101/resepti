# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import RecipeIngredient, RecipeUnit, RecipeClass, Recipe, RecipeTable


class IngredientInline(admin.TabularInline):
    model = RecipeTable


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ["name"]


@admin.register(RecipeUnit)
class RecipeUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'name')
    search_fields = ['unit', 'name']


@admin.register(RecipeClass)
class RecipeClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'slug', 'class_visibility')
    list_filter = ('class_visibility',)
    search_fields = ['class_name']
    readonly_fields = ['slug']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe_name',
        'recipe_class',
        'recipe_picture',
        'recipe_visibility',
    )
    list_filter = ('recipe_class', 'recipe_visibility')
    search_fields = ["recipe_name"]
    autocomplete_fields = ['recipe_class']
    inlines = [IngredientInline]


@admin.register(RecipeTable)
class RecipeTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'recipe_ingredient',
        'recipe_ingredient_amount',
        'recipe_ingredient_unit',
    )
    # raw_id_fields = ('recipe', 'recipe_ingredient', 'recipe_ingredient_unit')
    autocomplete_fields = ["recipe", "recipe_ingredient", "recipe_ingredient_unit"]
