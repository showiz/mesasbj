# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    list_filter = ('nombre',)
    
    # Campos para mostrar del Usuario:
    fieldsets = (
        (None, {'fields': ('email', 'password', 'rut','dig_rut')}),
        #(_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions',)}), # user_permissions
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # Campos para el registro del Usuario:
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'rut', 'dig_rut','nombre', 'apellido', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'rut','dig_rut', 'nombre', 'apellido', 'is_staff')
    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('email',)