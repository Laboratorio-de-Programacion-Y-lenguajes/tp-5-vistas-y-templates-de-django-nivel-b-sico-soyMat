from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion

# Vista para la pagina de inicio
class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"

    def get_context_data(self, **kwargs):
        # Recuperamos el contexto base y le sumamos nuestros datos
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Portal de publicaciones"
        contexto["mensaje"] = "Bienvenido/a al sitio"
        return contexto


# Vista para listar todas las publicaciones
class PublicacionListView(ListView):
    model = Publicacion
    context_object_name = "publicacion_list"


# Vista para ver el detalle de una publicacion especifica
class PublicacionDetailView(DetailView):
    model = Publicacion
    context_object_name = "publicacion"
    # Le decimos a Django como se llama el parametro en la URL
    pk_url_kwarg = "publicacion_id"