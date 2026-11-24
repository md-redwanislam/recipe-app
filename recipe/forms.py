from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Instruction


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "cover_image",
            "status",
        ]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "quantity",
            "unit",
            "name",
        ]


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ["step_number", "description"]


IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=5,
    can_delete=True,
)

InstructionFormSet = inlineformset_factory(
    Recipe,
    Instruction,
    form=InstructionForm,
    extra=5,
    can_delete=True,
)

