from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from account import forms
from account import models


class UserAdmin(BaseUserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    list_display = [
        'full_name',
        'email',
        'phone',
        'is_admin',
    ]
    list_filter = [
        'is_admin',
    ]
    fieldsets = [
        (
            None, {
                'fields': (
                    'full_name',
                )
            }
        ),
        (
            'Authentications', {
                'fields': (
                    'email',
                    'phone',
                    'password',
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active',
                    'is_admin',
                    'last_login',
                )
            }
        ),
    ]
    add_fieldsets = [
        (
            None, {
                'fields': (
                    'full_name',
                )
            }
        ),
        (
            'Information', {
                'fields': (
                    'phone',
                    'email',
                )
            }
        ),
        (
            'Password', {
                'fields': (
                    'password1',
                    'password2',
                )
            }
        ),
    ]
    search_fields = [
        'full_name',
        'email',
        'phone',
    ]
    ordering = [
        'full_name',
    ]
    filter_horizontal = []


admin.site.unregister(Group)
admin.site.register(models.User, UserAdmin)
