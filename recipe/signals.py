from django.db import transaction
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .models import Recipe


@receiver(pre_save, sender=Recipe)
def store_old_cover_image(sender, instance, **kwargs):
    if not instance.pk:
        return

    old_recipe = Recipe.objects.filter(pk=instance.pk).first()

    if old_recipe and old_recipe.cover_image:
        instance._old_cover_image_name = old_recipe.cover_image.name
        instance._old_cover_image_storage = old_recipe.cover_image.storage


@receiver(post_save, sender=Recipe)
def delete_old_cover_image(sender, instance, **kwargs):
    old_name = getattr(instance, "_old_cover_image_name", None)
    old_storage = getattr(instance, "_old_cover_image_storage", None)

    if old_name and old_name != instance.cover_image.name:
        transaction.on_commit(
            lambda: old_storage.delete(old_name)
        )


@receiver(post_delete, sender=Recipe)
def delete_recipe_cover_image(sender, instance, **kwargs):
    if instance.cover_image:
        storage = instance.cover_image.storage
        image_name = instance.cover_image.name

        transaction.on_commit(
            lambda: storage.delete(image_name)
        )