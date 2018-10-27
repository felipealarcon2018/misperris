from django.urls import path
from .views import home, galeria, formulario,listar_mascotas,eliminar_mascota, modificar_mascota,formulario_m, listar_postulante ,modificar_postulante, eliminar_postulante
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('listar-mascotas/', listar_mascotas, name="listado_mascotas"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),  
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"), 
    path('formulario-m/',formulario_m, name="formulario_m"),
    path('listar-postulantes/', listar_postulante, name="listar_postulante"),
    path('modificar-postulante/<id>/', modificar_postulante, name="modificar_postulante"), 
    path('eliminar-postulante/<id>',eliminar_postulante, name="eliminar_postulante" )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)