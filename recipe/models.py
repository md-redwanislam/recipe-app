import uuid

from django.db import models
from django.conf import settings


# Create your models here.


class UUIDModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class Recipe(UUIDModel):

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
 
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    cover_image = models.ImageField(
        upload_to="recipe_covers/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Ingredient(UUIDModel):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}".strip()


class Instruction(UUIDModel):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="instructions"
    )

    step_number = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ["step_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "step_number"],
                name="unique_recipe_instruction_step"
            )
        ]

    def __str__(self):
        return f"{self.recipe.title} - Step {self.step_number}"



