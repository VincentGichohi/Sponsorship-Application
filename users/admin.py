from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
    #The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the user model.
    # These override the definition on the base UserAdmin
    # That references specific fields on auth.user
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add fieldsets is not a standard ModelAdmin attribute. UserAdmin
    #overrides get_fieldsets to use this attribute when creating a user
