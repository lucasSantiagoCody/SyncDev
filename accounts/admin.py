from django.contrib import admin
from .models import CustomUser, Profile
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff','is_superuser']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
 