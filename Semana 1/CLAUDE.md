# Laboratorio 01 — Introducción a Django

Instrucciones para construir el laboratorio de la Semana 1 del curso
**Desarrollo de Aplicaciones Empresariales** (4 - C24 - Sección CD).
Fuente: `GLAB-S01-YBESTARD-2026-02.docx`. Estudiante: **Renzo León**.

## Objetivo

Construir la primera versión del *Sistema Empresarial*: una aplicación Web en
Django que gestiona un catálogo simple de ítems. Este proyecto es la base de las
siguientes sesiones del curso, así que la estructura debe quedar limpia y escalable.

Capacidades que evalúa el laboratorio:

1. Identificar las características de Django como framework de desarrollo web.
2. Instalar y configurar el entorno (Python, entorno virtual y Django).
3. Crear una aplicación Web reconociendo proyecto, app, modelos, vistas, URLs y administrador.

## Entorno de este equipo

- Windows 11, shell **PowerShell**. No uses sintaxis bash (`&&`, `source`, `mkdir -p`).
- Python **no** está en el PATH como `python`: usa el lanzador `py` para crear el
  entorno virtual, y después el intérprete del venv por ruta absoluta.
- Django 5 (5.2.17 al momento de armarlo), SQLite, Visual Studio Code y Git.

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install "django>=5,<6"
```

## Estructura obligatoria

El manual exige que `manage.py` quede en `src/` y la configuración en `src/config/`.
Eso se consigue con el punto final en `startproject`; sin él Django crea una carpeta
anidada de más.

```
Semana 1/
└── django_project/
    ├── venv/                  # entorno virtual (fuera de src/, no se versiona)
    ├── README.md
    ├── .gitignore
    └── src/
        ├── manage.py
        ├── requirements.txt
        ├── db.sqlite3
        ├── config/            # settings.py, urls.py, asgi.py, wsgi.py
        ├── core/              # app principal
        ├── templates/
        │   ├── base.html
        │   └── core/item_list.html
        └── static/css/styles.css
```

## Los 10 ejercicios

Desarróllalos **en orden**. Cada paso debe quedar evidenciado con una captura de
pantalla y una breve explicación; no copies comandos sin comprenderlos.

1. **Entorno.** Crear `django_project`, el venv y dentro la carpeta `src/`.
2. **Instalar Django.** Con el venv activado, instalar Django 5 y verificar la versión.
3. **Proyecto `config`.** Desde `src/`, `django-admin startproject config .`
4. **App `core`.** `manage.py startapp core` y registrarla en `INSTALLED_APPS`.
5. **Modelo `Item`.** Campos `name` (texto), `description` (texto largo, opcional)
   y `created_at` (fecha/hora automática). Generar y aplicar migraciones.
6. **Vista y URLs.** Vista `item_list` que obtenga todos los `Item` y los pase a una
   plantilla; `core/urls.py` enlazado desde `config/urls.py` con `include()`.
7. **Plantillas.** `base.html` con la estructura general y `core/item_list.html` que
   herede de ella y liste los ítems con `{% for %}` y `{% empty %}`.
8. **Administrador y datos.** Registrar `Item` en `core/admin.py`, crear superusuario
   y registrar al menos **dos** ítems de prueba.
9. **Verificar.** `runserver` y comprobar que `/` muestra el listado y `/admin/` funciona.
10. **Documentar y subir.** `requirements.txt`, `README.md` y repositorio en GitHub.

### Retos opcionales

- Estilos CSS en la plantilla base.
- Interactividad en el frontend (por ejemplo, un buscador con JavaScript).
- Con apoyo de IA, endpoints (API) para `Item` consumidos desde un frontend vanilla o React.

## Convenciones de código

- Todo el contenido visible al usuario en **español**; nombres de código en inglés
  (`Item`, `item_list`, `name`, `created_at`), como en la documentación de Django.
- Docstring breve en cada modelo, vista y clase de configuración.
- En el modelo: `__str__` que devuelva el nombre, y `class Meta` con `verbose_name`,
  `verbose_name_plural` y `ordering`.
- En el admin: `list_display`, `search_fields` y `list_filter`.
- En `core/urls.py` definir `app_name = 'core'` y referenciar las rutas en las
  plantillas con `{% url 'core:item_list' %}`, nunca con rutas fijas.
- PEP 8: 4 espacios, líneas de hasta 79-99 caracteres, imports agrupados.

## Ajustes de `settings.py`

Además de registrar `'core'` en `INSTALLED_APPS`:

- `TEMPLATES['DIRS'] = [BASE_DIR / 'templates']`
- `STATICFILES_DIRS = [BASE_DIR / 'static']`
- `LANGUAGE_CODE = 'es'` y `TIME_ZONE = 'America/Lima'`

Ojo: aquí `BASE_DIR` apunta a `src/`, porque el proyecto se creó con el punto final.

## Comandos frecuentes

Desde `django_project\src`, con el entorno virtual activado:

```powershell
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
```

- Catálogo: http://127.0.0.1:8000/
- Administración: http://127.0.0.1:8000/admin/

## Errores a evitar

- **Olvidar el punto** en `django-admin startproject config .` → estructura incorrecta.
- **Instalar sin el venv activado** → Django queda en el sistema y el proyecto deja
  de ser reproducible.
- **Abrir los `.html` directamente en el navegador**: se ven las etiquetas
  `{% block %}` en crudo. Las plantillas solo se interpretan si las sirve Django.
- **Versionar `venv/` o `db.sqlite3`**: deben estar en `.gitignore`.
- `created_at` usa `auto_now_add=True`, por lo que no es editable en el administrador.

## Entregables y rúbrica (20 puntos)

| Criterio | Pts |
|---|---|
| Creación de la página web en Django | 4 |
| Funcionamiento de la página web | 4 |
| Tarea (informe con capturas y explicaciones) | 6 |
| Buenas prácticas de programación | 2 |
| Observaciones y conclusiones | 4 |

- **Informe** en la plantilla del laboratorio: una captura por ejercicio con una
  breve explicación. Subirlo a Canvas **en formato PDF**.
- **Repositorio**: enlace de GitHub con el proyecto completo.
- **Sustentación**: hay que poder explicar y ejecutar el proyecto en clase.

Como la mitad de la nota vive en la redacción, cierra siempre con observaciones y
conclusiones propias, no genéricas: qué falló, qué se entendió y por qué.

## Material de apoyo ya generado

- `INFORME_Lab01.md` — explicación de los 10 ejercicios, observaciones y conclusiones.
- `Capturas informe\` — capturas nombradas por ejercicio (`EjNN_n_...`) con sus
  pies de foto en `_LEEME_orden_de_las_capturas.md`.

## Seguridad del laboratorio

Prohibido manipular hardware, conexiones eléctricas o de red, e ingerir alimentos
y bebidas. Maletines y mochilas en el lugar destinado. Dejar mesa y silla limpias.
