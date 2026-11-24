from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import (
    RecipeForm,
    IngredientFormSet,
    InstructionFormSet,
)


from django.db.models import Q
from .models import Recipe


# Create your views here.


@login_required(login_url='/auth/login/')
def create_recipe_view(request):
    if request.method == "POST":
        recipe_form = RecipeForm(
            request.POST,
            request.FILES,
        )

        ingredient_formset = IngredientFormSet(
            request.POST,
            prefix="ingredients",
        )

        instruction_formset = InstructionFormSet(
            request.POST,
            prefix="instructions",
        )

        if (
            recipe_form.is_valid()
            and ingredient_formset.is_valid()
            and instruction_formset.is_valid()
        ):
            with transaction.atomic():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user
                recipe.save()

                ingredient_formset.instance = recipe
                ingredient_formset.save()

                instruction_formset.instance = recipe
                instruction_formset.save()

            return redirect("recipe_list")

    else:
        recipe_form = RecipeForm()

        ingredient_formset = IngredientFormSet(
            prefix="ingredients",
        )

        instruction_formset = InstructionFormSet(
            prefix="instructions",
        )

    return render(
        request,
        "create_recipe.html",
        {
            "recipe_form": recipe_form,
            "ingredient_formset": ingredient_formset,
            "instruction_formset": instruction_formset,
        },
    )


def recipe_list_view(request):
    recipes = Recipe.objects.filter(
        status=Recipe.Status.PUBLISHED
    )

    return render(
        request,
        "recipe_list.html",
        {"recipes": recipes},
    )


def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(
        Recipe.objects.prefetch_related(
            "ingredients",
            "instructions",
        ),
        id=recipe_id,
    )

    # Draft recipes are visible only to their owners.
    if (
        recipe.status == Recipe.Status.DRAFT
        and recipe.author != request.user
    ):
        from django.http import Http404
        raise Http404("Recipe not found")

    return render(
        request,
        "recipe_detail.html",
        {"recipe": recipe},
    )



@login_required
def edit_recipe_view(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        author=request.user,
    )

    if request.method == "POST":
        recipe_form = RecipeForm(
            request.POST,
            request.FILES,
            instance=recipe,
        )

        ingredient_formset = IngredientFormSet(
            request.POST,
            instance=recipe,
            prefix="ingredients",
        )

        instruction_formset = InstructionFormSet(
            request.POST,
            instance=recipe,
            prefix="instructions",
        )

        if (
            recipe_form.is_valid()
            and ingredient_formset.is_valid()
            and instruction_formset.is_valid()
        ):
            with transaction.atomic():
                recipe_form.save()
                ingredient_formset.save()
                instruction_formset.save()

            return redirect("recipe_detail", recipe_id=recipe.id)

    else:
        recipe_form = RecipeForm(instance=recipe)

        ingredient_formset = IngredientFormSet(
            instance=recipe,
            prefix="ingredients",
        )

        instruction_formset = InstructionFormSet(
            instance=recipe,
            prefix="instructions",
        )

    return render(
        request,
        "edit_recipe.html",
        {
            "recipe": recipe,
            "recipe_form": recipe_form,
            "ingredient_formset": ingredient_formset,
            "instruction_formset": instruction_formset,
        },
    )



@login_required
def delete_recipe_view(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        author=request.user,
    )

    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")

    return render(
        request,
        "delete_recipe.html",
        {"recipe": recipe},
    )



