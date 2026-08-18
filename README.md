# Sistema Empresarial — Laboratorio 01

Aplicación Web en Django que gestiona un catálogo simple de ítems.
Curso: **Desarrollo de Aplicaciones Empresariales** (4 - C24 - Sección CD).

## Estructura del proyecto

```
django_project/
├── venv/                     # Entorno virtual de Python (no se sube a Git)
├── README.md
└── src/                      # Código fuente
    ├── manage.py
    ├── requirements.txt
    ├── db.sqlite3            # Base de datos SQLite (no se sube a Git)
    ├── config/               # Configuración del proyecto
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── core/                 # Aplicación principal
    │   ├── models.py         # Modelo Item
    │   ├── views.py          # Vista item_list
    │   ├── urls.py           # URLs de la app
    │   ├── admin.py          # Registro en el administrador
    │   └── migrations/
    ├── templates/
    │   ├── base.html
    │   └── core/item_list.html
    └── static/
        └── css/styles.css
```

## Modelo `Item`

| Campo         | Tipo            | Descripción                          |
|---------------|-----------------|--------------------------------------|
| `name`        | `CharField`     | Nombre del ítem (máx. 100 caracteres) |
| `description` | `TextField`     | Descripción larga, opcional           |
| `created_at`  | `DateTimeField` | Fecha de creación automática          |

## Instalación

Requisitos: Python 3.10 o superior.

```bash
git clone <url-del-repositorio>
cd django_project
python -m venv venv
venv\Scripts\activate          # En Linux/Mac: source venv/bin/activate
cd src
pip install -r requirements.txt
```

## Ejecución

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Catálogo de ítems: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

## Retos implementados

- Estilos CSS en la plantilla base (`static/css/styles.css`).
- Buscador de ítems en el frontend con JavaScript (`core/item_list.html`).

## Autor

Bestard Aroche, Yunior
