[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iPRTU322)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23853581)
# TP 5 · Vistas y Templates de Django - Nivel Básico

**Stack**: Python 3.13+, Django 5.1+, Django Templates, SQLite, `django.test.TestCase`, Git/GitHub Classroom  
**Entrega**: Repositorio de GitHub Classroom con autograding (GitHub Actions) — push a `main`.

---

## 1) Objetivo

Construir una aplicación web básica en Django que permita listar, visualizar y navegar información de una colección de publicaciones usando **vistas basadas en clases (CBV)** y **templates de Django**.

Relevancia profesional: las CBV permiten reutilizar comportamiento común (listar, mostrar detalle, manejar formularios) sin repetir lógica. Son el estándar en proyectos Django modernos y la base de las vistas genéricas. Este TP introduce el flujo completo **URL → CBV → contexto → template → HTML**.

Qué van a construir:

- Una app Django llamada `publicaciones`.
- Vistas basadas en clases:
  - `InicioView` (TemplateView) → página de bienvenida.
  - `PublicacionListView` (ListView) → listado de publicaciones.
  - `PublicacionDetailView` (DetailView) → detalle de una publicación.
- Templates reutilizando una plantilla base mediante herencia.
- Navegación entre páginas con el sistema de URLs de Django.
- Tests que validan respuestas HTTP, templates usados y contenido renderizado.
- Autograding con GitHub Actions.

---

## 2) Instalación de Python y pip (guía rápida)

### Windows (10/11)

1. Descargá Python 3.13.x desde [python.org/downloads](https://www.python.org/downloads/).
2. Durante la instalación, marcá **"Add Python to PATH"** → **Install Now**.
3. Verificá en PowerShell o CMD:
   ```bash
   python --version
   pip --version
   ```
   Si `python` no se reconoce, reiniciá la terminal o reinstalá marcando "Add Python to PATH".

### macOS

1. Instalá con [Homebrew](https://brew.sh/):
   ```bash
   brew install python@3.13
   ```
2. Verificá:
   ```bash
   python3 --version
   pip3 --version
   ```
> En macOS los comandos suelen ser `python3` y `pip3`.

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
pip3 --version
```

---

## 3) Setup del proyecto

### 1. Cloná tu repo de Classroom

```bash
git clone <URL-de-tu-repo>
cd <nombre-del-repo>
```

### 2. Creá un entorno virtual (recomendado)

**Windows (PowerShell)**:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalá dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicá migraciones

```bash
python manage.py migrate
```

### 5. Ejecutá el servidor

```bash
python manage.py runserver
```

Abrí en el navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 4) Objetivo funcional del TP

La aplicación representará un pequeño portal de publicaciones que permita:

1. Ver una **página de inicio** con bienvenida al sitio.
2. Ver una **lista de publicaciones** con título, autor y fecha.
3. Ver el **detalle de una publicación** según su `id`.
4. Navegar entre páginas usando links en los templates.
5. Reutilizar estructura común con un template base.

---

## 5) Estructura del repositorio

```text
.
├── manage.py
├── portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                        ← Completar include de la app
│   ├── asgi.py
│   └── wsgi.py
├── publicaciones/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      ← Provisto (no modificar)
│   ├── views.py                       ← Implementar aquí (CBV)
│   ├── urls.py                        ← Implementar aquí
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_views.py              ← Tests de vistas (provistos)
│   │   └── test_templates.py          ← Tests de templates (provistos)
│   └── migrations/
│       └── __init__.py
├── templates/
│   ├── base.html                      ← Completar aquí
│   └── publicaciones/
│       ├── inicio.html                ← Completar aquí
│       ├── publicacion_list.html      ← Completar aquí
│       └── publicacion_detail.html    ← Completar aquí
├── .github/
│   └── workflows/
│       └── autograding.yml
├── requirements.txt
├── README.md
└── .gitignore
```

> **Nota sobre nombres de templates**: Django CBV tiene convenciones automáticas.  
> `ListView` busca `<app>/<modelo>_list.html` → `publicaciones/publicacion_list.html`  
> `DetailView` busca `<app>/<modelo>_detail.html` → `publicaciones/publicacion_detail.html`

---

## 6) Archivos a completar

| Archivo | Qué implementar |
|--------|------------------|
| `portal/urls.py` | Incluir las rutas de `publicaciones` con `include()` |
| `publicaciones/views.py` | `InicioView`, `PublicacionListView`, `PublicacionDetailView` |
| `publicaciones/urls.py` | Rutas con `path()` y `.as_view()` |
| `templates/base.html` | Estructura HTML5 + navegación + `{% block content %}` |
| `templates/publicaciones/inicio.html` | Página de bienvenida extendiendo `base.html` |
| `templates/publicaciones/publicacion_list.html` | Listado con `{% for %}` extendiendo `base.html` |
| `templates/publicaciones/publicacion_detail.html` | Detalle extendiendo `base.html` |

---

## 7) Requisitos técnicos

### 7.1 Vistas (CBV)

#### `InicioView` → hereda de `TemplateView`
- Responde con HTTP `200`.
- Usa el template `publicaciones/inicio.html`.
- Sobreescribe `get_context_data()` para enviar al menos `titulo` y `mensaje`.

#### `PublicacionListView` → hereda de `ListView`
- Responde con HTTP `200`.
- Usa el template `publicaciones/publicacion_list.html`.
- Configura `model` y `context_object_name = "publicacion_list"`.

#### `PublicacionDetailView` → hereda de `DetailView`
- Responde con HTTP `200` si existe; `404` si no.
- Usa el template `publicaciones/publicacion_detail.html`.
- Configura `model`, `context_object_name = "publicacion"` y `pk_url_kwarg = "publicacion_id"`.

---

### 7.2 URLs

| URL | Vista | Nombre |
|-----|------|--------|
| `/` | `InicioView` | `inicio` |
| `/publicaciones/` | `PublicacionListView` | `lista_publicaciones` |
| `/publicaciones/<int:publicacion_id>/` | `PublicacionDetailView` | `detalle_publicacion` |

Usar `app_name = "publicaciones"` en `publicaciones/urls.py`.

---

### 7.3 Templates

#### `base.html`
- Estructura HTML5, título con variable de template.
- `header` con nombre del sitio.
- Navegación con links a inicio y publicaciones.
- `{% block content %}{% endblock %}`.

#### `inicio.html`
- Extiende `base.html`.
- Muestra `titulo` y `mensaje`.
- Link a la lista de publicaciones.

#### `publicacion_list.html`
- Extiende `base.html`.
- Itera `publicacion_list` con `{% for %}`.
- Muestra título, autor, fecha y link al detalle.
- Mensaje si no hay publicaciones.

#### `publicacion_detail.html`
- Extiende `base.html`.
- Muestra título, autor, contenido y fecha.
- Link para volver al listado.

---

## 8) Modelo provisto

```python
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
```

---

## 9) Diferencia clave: FBV vs CBV

| Aspecto | FBV | CBV |
|---------|-----|-----|
| Definición | función `def vista(request)` | clase que hereda de una vista genérica |
| Registro en URL | `views.vista` | `views.MiVista.as_view()` |
| Lógica extra | todo manual | sobreescribir métodos como `get_context_data()` |
| Reutilización | copiar código | herencia de clases |
| Cuándo usar | lógica muy custom | listados, detalles, formularios estándar |

```python
# FBV equivalente
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "publicaciones/publicacion_list.html", {"publicacion_list": publicaciones})

# CBV equivalente
class PublicacionListView(ListView):
    model = Publicacion
    context_object_name = "publicacion_list"
```

---

## 10) Tests

Ejecutalos con:

```bash
python manage.py test -v 2
```

O por módulo:

```bash
python manage.py test publicaciones.tests.test_views -v 2
python manage.py test publicaciones.tests.test_templates -v 2
```

---

## 11) Cómo se entrega

1. Completá `views.py` (CBV).
2. Completá `urls.py` del proyecto y de la app.
3. Completá los templates.
4. Corré:
   ```bash
   python manage.py migrate
   python manage.py test -v 2
   ```
5. Hacé **≥ 6 commits** significativos.
6. Hacé `push` a `main`.
7. Revisá GitHub → **Actions** para verificar ✅.

## 11b) Cargar datos de prueba

El repositorio incluye `populate_db.py` con 8 publicaciones de ejemplo para que puedas probar la app en el navegador sin cargar datos manualmente.

### Cómo usarlo

Asegurate de haber aplicado las migraciones primero:

```bash
python manage.py migrate
```

Luego ejecutá el script pasándoselo al shell de Django:

```bash
python manage.py shell < populate_db.py
```

Deberías ver una salida como esta:

```
🗑️  Base de datos limpia.
  ✅ 'Introducción a las Class Based Views en Django' — Ana García (2026-03-10)
  ✅ 'El sistema de templates de Django' — Carlos López (2026-03-15)
  ...
🎉 Se cargaron 8 publicaciones correctamente.

Resumen:
  Total en BD: 8 publicaciones
  Autores únicos: 6
  Más reciente: Introducción a las Class Based Views en Django
  Más antigua:  El patrón MVT de Django
```

Luego levantá el servidor y navegá a [http://127.0.0.1:8000/publicaciones/](http://127.0.0.1:8000/publicaciones/) para ver el listado con datos reales.

> **Nota**: el script limpia la base de datos antes de insertar. Si lo corrés dos veces, no genera duplicados.

> **Nota para tests**: los tests de autograding crean sus propios datos con `setUp()` y no dependen de este script. Podés correr `populate_db.py` solo para desarrollo local.

---

## 12) Commits sugeridos

```bash
feat: agrega InicioView con TemplateView
feat: implementa PublicacionListView
feat: agrega PublicacionDetailView con 404
feat: define rutas de la app publicaciones
feat: crea template base con navegación
feat: completa templates de listado y detalle
```

---

## 13) Evaluación automática

Al hacer push a `main`, GitHub Actions:
1. Instala dependencias.
2. Ejecuta migraciones.
3. Corre tests con Django.
4. Reporta ✅ o ❌ en la pestaña **Actions**.

---

## 14) Troubleshooting rápido

| Problema | Solución |
|----------|----------|
| `No module named django` | Activá el entorno virtual y corré `pip install -r requirements.txt` |
| `TemplateDoesNotExist` | Verificá nombre exacto del archivo (convención CBV: `_list`, `_detail`) |
| `NoReverseMatch` | Revisá `app_name` y `name=` en las rutas |
| `404` en URL válida | Verificá que `portal/urls.py` incluya las rutas de `publicaciones` |
| `OperationalError: no such table` | Corré `python manage.py migrate` |
| Tests fallan por contexto | Revisá `context_object_name` y `pk_url_kwarg` en las CBV |

---

## 15) Pistas útiles

### TemplateView con contexto extra
```python
from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Portal de publicaciones"
        context["mensaje"] = "Bienvenido/a al sitio"
        return context
```

### ListView básico
```python
from django.views.generic import ListView
from .models import Publicacion

class PublicacionListView(ListView):
    model = Publicacion
    context_object_name = "publicacion_list"
```

### DetailView con pk personalizado
```python
from django.views.generic import DetailView

class PublicacionDetailView(DetailView):
    model = Publicacion
    context_object_name = "publicacion"
    pk_url_kwarg = "publicacion_id"
```

### Registrar CBV en URLs
```python
path("publicaciones/", views.PublicacionListView.as_view(), name="lista_publicaciones"),
```

### Link nombrado en template
```django
<a href="{% url 'publicaciones:lista_publicaciones' %}">Ver publicaciones</a>
```

---

## 16) Flujo de trabajo recomendado

1. Revisá la estructura del proyecto y los tests provistos.
2. Implementá primero `publicaciones/urls.py` (aunque las vistas estén vacías).
3. Completá `views.py` vista por vista.
4. Conectá la app en `portal/urls.py`.
5. Completá `base.html` y luego los templates de cada vista.
6. Corré tests frecuentemente: `python manage.py test -v 2`.
7. Commits pequeños y significativos durante todo el proceso.

---

## 17) Relación con la materia

- **Módulo V**: Vistas y templates de Django como parte del patrón MVT.
- **Semana 7**: Introducción a vistas en Django.
- **Semana 8**: Introducción a templates de Django.
- **Semana 9**: Vistas avanzadas y vistas genéricas → base para la App Integradora #1.

---

## 18) Recursos oficiales recomendados

- [Django Docs · Class-based views intro](https://docs.djangoproject.com/en/5.1/topics/class-based-views/intro/)
- [Django Docs · Built-in CBV API (TemplateView, ListView, DetailView)](https://docs.djangoproject.com/en/5.1/ref/class-based-views/)
- [Django Docs · The Django template language](https://docs.djangoproject.com/en/5.1/ref/templates/language/)
- [Django Docs · URL dispatcher](https://docs.djangoproject.com/en/5.1/topics/http/urls/)
- [Django Docs · Tutorial part 3 (views)](https://docs.djangoproject.com/en/5.1/intro/tutorial03/)

---

## 19) Criterios de aprobación

- [ ] Las tres CBV implementadas correctamente
- [ ] Todas las rutas funcionando con `.as_view()`
- [ ] Templates con herencia de `base.html`
- [ ] Navegación funcional entre las tres páginas
- [ ] Tests pasando (autograding ✅)
- [ ] Código claro con nombres descriptivos
- [ ] ≥ 6 commits significativos