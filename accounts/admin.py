from django.contrib import admin
from .models import CustomUser

# Register your models here.



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    # Columns displayed in the user list
    list_display = (
        "id",
        "email",
        "name",
        "phone",
        "is_active",
        "is_staff",
        "date_joined",
    )

    # Sidebar filters
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )

    # Search functionality
    search_fields = (
        "email",
        "name",
        "phone",
    )

    # Default ordering
    ordering = ("email",)

    # Number of users per page
    list_per_page = 25

    # Fields that should not be directly editable
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )

    # Fields displayed when editing a user
    fields = (
        "id",
        "email",
        "name",
        "phone",
        "bio",
        "profile_picture",
        "is_active",
        "is_staff",
        "is_superuser",
        "groups",
        "user_permissions",
        "date_joined",
        "last_login",
    )

    filter_horizontal = (
        "groups",
        "user_permissions",
    )