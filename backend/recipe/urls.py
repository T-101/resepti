from django.urls import path

from recipe.views import LandingPageView, RecipeView, RecipeTypeView, SearchView

app_name = "recipe"

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing-page"),
    path('recipe/<slug:slug>/', RecipeView.as_view(), name="detail"),
    path('type/<slug:slug>/', RecipeTypeView.as_view(), name="types"),
    path('search/', SearchView.as_view(), name="search")
]
