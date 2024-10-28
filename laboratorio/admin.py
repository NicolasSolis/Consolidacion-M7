from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

admin.site.site_header = 'Consolidacion 7 Django'
admin.site.index_title = 'Panel de control Proyecto Laboratorio'
admin.site.site_title = 'Administrador Django'

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'pais')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'especialidad')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)