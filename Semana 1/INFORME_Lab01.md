# Informe — Laboratorio 01: Introducción a Django

**Curso:** Desarrollo de Aplicaciones Empresariales — 4 - C24 - Sección CD
**Estudiante:** Renzo León

> Texto de apoyo para la plantilla Word del laboratorio. Cada ejercicio indica
> **qué capturar** y la **explicación** que acompaña a la captura.

---

## Ejercicio 1 y 2 — Preparar el entorno e instalar Django

**Captura:** terminal con la creación del entorno virtual, el prompt `(venv)` activo y la salida de `python -m django --version`.

**Explicación:** Se creó la carpeta `django_project` como raíz del laboratorio y dentro de ella un entorno virtual con `python -m venv venv`. El entorno virtual aísla las dependencias de este proyecto de las del sistema, de modo que la versión de Django instalada aquí no interfiere con otros proyectos. Con el entorno activado se instaló Django mediante `pip` y se verificó la instalación, obteniendo la versión **5.2.17**. También se creó la carpeta `src/`, que contendrá únicamente el código fuente, separándolo del entorno virtual.

**Comandos:**
```bash
mkdir django_project
cd django_project
python -m venv venv
venv\Scripts\activate
mkdir src
pip install django
python -m django --version
```

---

## Ejercicio 3 — Crear el proyecto con configuración separada

**Captura:** el explorador de archivos de VS Code mostrando `src/manage.py` y la carpeta `src/config/`.

**Explicación:** Situado dentro de `src/`, se ejecutó `django-admin startproject config .`. El punto final es clave: indica que el proyecto se cree en el directorio actual en lugar de generar una carpeta contenedora extra. El resultado es que `manage.py` queda en `src/` y toda la configuración (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`) queda agrupada en `src/config/`. Esta separación permite que el nombre del proyecto no se confunda con el de la carpeta raíz.

**Comando:**
```bash
django-admin startproject config .
```

---

## Ejercicio 4 — Crear y registrar la aplicación core

**Captura:** la carpeta `src/core/` generada y el bloque `INSTALLED_APPS` de `settings.py` con `'core'` añadido.

**Explicación:** Django organiza la funcionalidad en aplicaciones reutilizables. Se creó la app `core` con `python manage.py startapp core` y se registró en la lista `INSTALLED_APPS` de `src/config/settings.py`. Sin este registro, Django ignoraría los modelos, migraciones y plantillas de la aplicación. Adicionalmente se configuró `TEMPLATES['DIRS']` para usar una carpeta de plantillas común y `STATICFILES_DIRS` para los archivos estáticos, y se ajustaron `LANGUAGE_CODE = 'es'` y `TIME_ZONE = 'America/Lima'`.

---

## Ejercicio 5 — Definir el modelo Item

**Captura:** el archivo `core/models.py` y la salida de `makemigrations` + `migrate`.

**Explicación:** En `src/core/models.py` se definió el modelo `Item` con tres campos: `name` (`CharField`, obligatorio), `description` (`TextField` con `blank=True`, por tanto opcional) y `created_at` (`DateTimeField` con `auto_now_add=True`, que registra la fecha automáticamente al crear el registro). Se añadió el método `__str__` para que el objeto se muestre por su nombre en el administrador, y una clase `Meta` con nombres legibles en español y ordenamiento descendente por fecha. `makemigrations` traduce el modelo a instrucciones de base de datos y `migrate` las aplica sobre SQLite.

**Comandos:**
```bash
python manage.py makemigrations core
python manage.py migrate
```

---

## Ejercicio 6 — Crear la vista y las URLs

**Captura:** `core/views.py`, `core/urls.py` y `config/urls.py`.

**Explicación:** Se implementó la vista `item_list` en `src/core/views.py`, que consulta todos los registros con `Item.objects.all()` y los entrega a la plantilla mediante `render()`. Las rutas de la aplicación se declararon en `core/urls.py` con un `app_name = 'core'` que permite referenciarlas como `core:item_list`, y se enlazaron desde `src/config/urls.py` con `include('core.urls')`. Este esquema mantiene las URLs de cada app independientes y hace que el proyecto sea más fácil de escalar.

---

## Ejercicio 7 — Crear las plantillas

**Captura:** `templates/base.html`, `templates/core/item_list.html` y la página renderizada en el navegador.

**Explicación:** Se creó `base.html` con la estructura HTML general (cabecera, navegación, contenedor principal y pie), definiendo bloques `{% block title %}` y `{% block content %}`. La plantilla `core/item_list.html` hereda de ella con `{% extends 'base.html' %}` y rellena solo el bloque de contenido, evitando duplicar el HTML común. El listado usa `{% for item in items %}` para recorrer los ítems y `{% empty %}` para mostrar un mensaje cuando la lista está vacía.

> **Nota:** las etiquetas `{% ... %}` solo se interpretan cuando la página es servida por el servidor de desarrollo de Django. Si se abre el archivo `.html` directamente en el navegador, se muestran en crudo porque el navegador no ejecuta el motor de plantillas.

---

## Ejercicio 8 — Configurar el administrador y cargar datos

**Captura:** `core/admin.py`, la creación del superusuario y el panel `/admin/` con los dos ítems registrados.

**Explicación:** El modelo `Item` se registró en `src/core/admin.py` usando el decorador `@admin.register(Item)` junto con una clase `ItemAdmin` que define `list_display`, `search_fields` y `list_filter` para mejorar la usabilidad del panel. Se creó un superusuario con `createsuperuser` y, desde el panel de administración, se registraron dos ítems de prueba: *Laptop Lenovo ThinkPad* y *Monitor Dell 24 pulgadas*.

---

## Ejercicio 9 — Verificar el funcionamiento

**Captura:** la terminal con `runserver` activo, la página `http://127.0.0.1:8000/` mostrando el listado y el panel `/admin/`.

**Explicación:** Se levantó el servidor de desarrollo con `python manage.py runserver`. La página principal muestra correctamente el listado de ítems con su nombre, descripción y fecha de creación, y el panel de administración permite gestionarlos. Adicionalmente se ejecutó `python manage.py test`, con **6 pruebas superadas** que validan el modelo y la vista.

**Comandos:**
```bash
python manage.py runserver
python manage.py test
```

---

## Ejercicio 10 — Documentar y subir el proyecto

**Captura:** `requirements.txt`, `README.md` y el repositorio en GitHub.

**Explicación:** Se generó `requirements.txt` con `pip freeze`, que fija las versiones exactas de las dependencias para que el proyecto pueda reproducirse en otra máquina. Se redactó un `README.md` explicando la estructura de carpetas, el modelo de datos y los pasos de instalación y ejecución. Se añadió un `.gitignore` para excluir el entorno virtual, los `__pycache__` y la base de datos SQLite, y finalmente el proyecto se versionó con Git y se subió a GitHub.

---

## Retos opcionales implementados

1. **Estilos CSS:** se añadió `static/css/styles.css`, enlazado desde `base.html` con `{% load static %}`, que da formato a la cabecera, las tarjetas de ítems y el pie de página.
2. **Interactividad en el frontend:** se implementó un buscador en JavaScript que filtra el listado en tiempo real conforme se escribe, sin recargar la página.

---

## Observaciones

- El punto final en `django-admin startproject config .` es determinante: sin él Django genera una carpeta anidada adicional y la estructura no coincide con la pedida en el laboratorio.
- Las etiquetas de plantilla (`{% block %}`, `{% for %}`, `{% load static %}`) solo se procesan cuando la página se sirve a través del servidor de Django. Abrir el archivo HTML directamente muestra el código sin interpretar; esto no indica un error en el proyecto.
- Al definir la carpeta de plantillas en `TEMPLATES['DIRS']` fue necesario apuntar a `BASE_DIR / 'templates'`, ya que `BASE_DIR` corresponde a `src/`. Lo mismo aplicó a `STATICFILES_DIRS` para que el CSS fuera localizado.
- El campo `created_at` con `auto_now_add=True` es de solo lectura: no aparece como editable en el formulario del administrador, porque Django lo asigna automáticamente al momento de la creación.
- Trabajar con el entorno virtual activado es indispensable; ejecutar `pip install` sin activarlo instala Django a nivel del sistema y el proyecto deja de ser reproducible.
- El uso de `app_name` junto con `{% url 'core:item_list' %}` evita escribir rutas fijas en las plantillas: si la URL cambia, el enlace sigue funcionando sin tocar el HTML.

---

## Conclusiones

1. Django es un framework web de alto nivel que aplica el patrón **MVT** (Modelo–Vista–Plantilla), lo que permite separar con claridad los datos, la lógica de negocio y la presentación. Esta separación se comprobó en la práctica: el modelo `Item` define la estructura de datos, la vista `item_list` resuelve la lógica y las plantillas se ocupan exclusivamente de la interfaz.
2. El uso de un entorno virtual garantiza que las dependencias del proyecto queden aisladas y sean reproducibles. Junto con `requirements.txt`, cualquier persona puede reconstruir el mismo entorno de trabajo con un solo comando.
3. El **ORM** de Django permite trabajar con la base de datos mediante clases y objetos de Python, sin escribir SQL. El sistema de migraciones lleva un control versionado de los cambios en el esquema, lo que hace que la evolución del modelo sea segura y trazable.
4. El panel de administración generado automáticamente representa un ahorro significativo de trabajo: con solo registrar el modelo se obtuvo una interfaz completa de altas, bajas, modificaciones y búsquedas.
5. La herencia de plantillas (`extends` y `block`) evita la duplicación de código HTML y centraliza los cambios de diseño en un único archivo, lo que facilita el mantenimiento a medida que el sistema crezca.
6. La organización del proyecto en `config/` para la configuración y aplicaciones independientes como `core` establece una base escalable, sobre la cual se podrán añadir nuevos módulos del Sistema Empresarial en las siguientes sesiones del curso.
