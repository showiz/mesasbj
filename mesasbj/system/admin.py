from django.contrib import admin

# Register your models here.

from .models import Categoria, Mesa

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Categoria, CategoriaAdmin)

class MesaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Mesa, MesaAdmin)
