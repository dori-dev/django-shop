from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account import forms


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
    readonly_fields = [
        'last_login',
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
                    'last_login',
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active',
                    'is_admin',
                    'is_superuser',
                    'groups',
                    'user_permissions',
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
    filter_horizontal = [
        'groups',
        'user_permissions',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form
