from django.urls import path
from . import views

app_name = "publicaciones"

#rutas de nuestra aplicacion para conectar con las vistas
urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path("publicaciones/", views.PublicacionListView.as_view(), name="lista_publicaciones"),
    path("publicaciones/<int:publicacion_id>/", views.PublicacionDetailView.as_view(), name="detalle_publicacion"),
]