# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Ingredient, IngredientUnit, RecipeClass, Recipe, RecipeTable


class IngredientInline(admin.TabularInline):
    model = RecipeTable
    autocomplete_fields = ["ingredient", "ingredient_unit"]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ["name"]


@admin.register(IngredientUnit)
class IngredientUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'name')
    search_fields = ['unit', 'name']


@admin.register(RecipeClass)
class RecipeClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ['name']
    readonly_fields = ['slug']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'recipe_class',
        'picture',
        'is_visible',
    )
    list_filter = ('recipe_class', 'is_visible')
    search_fields = ["name"]
    autocomplete_fields = ['recipe_class']
    inlines = [IngredientInline]


@admin.register(RecipeTable)
class RecipeTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'ingredient',
        'ingredient_amount',
        'ingredient_unit',
    )
    autocomplete_fields = ["recipe", "ingredient", "ingredient_unit"]
