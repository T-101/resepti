from django.db.models.functions import Lower
from django.views.generic import TemplateView, DetailView, ListView

from recipe.models import Recipe, RecipeClass


class LandingPageView(ListView):
    template_name = "recipe/index.html"
    model = RecipeClass
    queryset = RecipeClass.objects.order_by(Lower("class_name"))


class RecipeView(DetailView):
    model = Recipe
    queryset = Recipe.objects.prefetch_related("recipe_tables__recipe_ingredient", "recipe_tables__recipe_ingredient_unit").all()


class RecipeTypeView(ListView):
    model = Recipe

    def get_queryset(self):
        return self.model.objects.filter(recipe_class__slug=self.kwargs.get("slug")).order_by(Lower("recipe_name"))


class SearchView(ListView):
    model = Recipe

    def get_queryset(self):
        return self.model.objects.filter(recipe_name__icontains=self.request.GET.get("q")).order_by(Lower("recipe_name"))
