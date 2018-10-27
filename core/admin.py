from django.contrib import admin
from .models import Raza, Estado, Mascotas, Ciudad,Region,Postulante,Tipo_vivienda
# Register your models here.

class MascotasAdmin(admin.ModelAdmin):
    list_display = ('nombre','genero', 'raza','fecha_nacimiento','fecha_ingreso','estado')
    search_fields = ['nombre', 'fecha_ingreso']
    list_filter = ('fecha_ingreso',)

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_nac', 'telefono','email','ciudad','region','tipo_vivienda')
    search_fields = ['nombre', 'fecha_nac']
    list_filter = ('fecha_nac',)


admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascotas, MascotasAdmin)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(Tipo_vivienda)
admin.site.register(Postulante, PostulanteAdmin)