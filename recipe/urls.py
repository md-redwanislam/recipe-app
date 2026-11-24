from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_recipe_view, name="create_recipe"),
    
    path("<uuid:recipe_id>/", views.recipe_detail_view, name="recipe_detail"),
    path("<uuid:recipe_id>/edit/", views.edit_recipe_view, name="edit_recipe"),
    path("<uuid:recipe_id>/delete/", views.delete_recipe_view, name="delete_recipe"),
]
