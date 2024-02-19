from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Users
from .forms import UserChangeForm, UserCreationForm


@admin.register(Users)
class UsersAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (
            "Cargo",
            {
                "fields": ("role",),
            },
        ),
    )
