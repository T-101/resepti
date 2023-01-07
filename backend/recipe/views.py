from django.db.models import Q, Count
from django.db.models.functions import Lower
from django.views.generic import TemplateView, DetailView, ListView

from recipe.models import Recipe, RecipeClass


class LandingPageView(ListView):
    template_name = "recipe/index.html"
    model = RecipeClass
    queryset = RecipeClass.objects.annotate(Count("recipies")).order_by(Lower("name"))


class RecipeView(DetailView):
    model = Recipe
    queryset = Recipe.objects \
        .filter(is_visible=True) \
        .prefetch_related("recipe_tables__ingredient", "recipe_tables__ingredient_unit") \
        .select_related("recipe_class") \
        .all()


class RecipeTypeView(ListView):
    model = Recipe

    def get_queryset(self):
        return self.model.objects\
            .filter(is_visible=True) \
            .filter(recipe_class__slug=self.kwargs.get("slug")).order_by(Lower("name"))


class SearchView(ListView):
    model = Recipe

    def get_queryset(self):
        query = self.request.GET.get("q")
        return self.model.objects \
            .filter(is_visible=True) \
            .filter(Q(name__icontains=query) | Q(recipe_tables__ingredient__name__icontains=query)) \
            .order_by(Lower("name")).distinct()
