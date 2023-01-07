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
    list_display = ('id', 'name', 'slug', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ['name']
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
        'ingredient',
        'ingredient_amount',
        'ingredient_unit',
    )
    autocomplete_fields = ["recipe", "ingredient", "ingredient_unit"]
