from django.contrib import admin
from .models import tipoUva, regionVitivinicola, varietal

# Register your models here.

@admin.register(tipoUva)
class tipoUvaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(regionVitivinicola)
class regionVitivinicolaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(varietal)
class varietalAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'porcentajeComposicion', 'tipoUva', 'regionVitivinicola')
    list_filter = ('tipoUva', 'regionVitivinicola')
    search_fields = ('descripcion', 'tipoUva__nombre', 'regionVitivinicola__nombre')