from django.urls import path

from recipe.views import LandingPageView, RecipeView, RecipeTypeView, SearchView, InfoView, RecipeIngredientView

app_name = "recipe"

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing-page"),
    path('info/', InfoView.as_view(), name="info"),
    path('r/<slug:slug>/', RecipeView.as_view(), name="detail"),
    path('i/<slug:slug>/', RecipeIngredientView.as_view(), name="ingredient-detail"),
    path('type/<slug:slug>/', RecipeTypeView.as_view(), name="types"),
    path('search/', SearchView.as_view(), name="search")
]
