from django.contrib.auth import admin as auth_admin, models as auth_models
from django.contrib import admin
from django.contrib.admin import register
from django.utils.translation import gettext_lazy as _
from . import models

admin.site.unregister(auth_models.Group)


@register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff'),
        }),
    )

    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('__str__', 'email', 'is_staff')
