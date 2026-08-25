# Orden de las capturas en el informe

Los archivos ya están numerados: al ordenarlos por nombre quedan en el mismo orden
en que van pegados en el Word. `EjNN_` indica el ejercicio y el dígito siguiente
el orden dentro de ese ejercicio.

Todas son **capturas reales de pantalla** (VS Code, Explorador de Windows, consola
PowerShell y navegador). Los renders de apoyo están aparte, en `Renders alternativos\`.

---

## Ejercicio 1 — Preparar el entorno de trabajo

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej01_1_terminal_venv_activado.png` | Entorno virtual activado: el prefijo `(venv)` y el intérprete de Python apuntando a `venv\Scripts\python.exe`. |
| `Ej01_2_explorador_django_project.png` | Estructura de `django_project`: carpetas `src/` y `venv/`, más `.gitignore` y `README`. |

## Ejercicio 2 — Instalar Django

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej02_1_terminal_pip_list_y_version.png` | Paquetes instalados en el entorno virtual y verificación de la versión: Django 5.2.17. |

## Ejercicio 3 — Crear el proyecto con configuración separada

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej03_1_terminal_arbol_config.png` | Árbol de `config/` con `settings.py`, `urls.py`, `asgi.py` y `wsgi.py`, y `manage.py` en `src/`. |
| `Ej03_2_explorador_src.png` | Contenido de `src/`: `config/`, `core/`, `static/`, `templates/`, `manage.py` y `requirements.txt`. |

## Ejercicio 4 — Crear y registrar la aplicación core

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej04_1_vscode_installed_apps.png` | `settings.py` con la aplicación `'core'` registrada al final de `INSTALLED_APPS`. |

## Ejercicio 5 — Definir el modelo Item

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej05_1_vscode_modelo_item.png` | Modelo `Item` con los campos `name`, `description` y `created_at`, junto al árbol completo del proyecto. |
| `Ej05_2_terminal_migraciones.png` | Migración `0001_initial` aplicada y tabla `core_item` creada en la base de datos. |

## Ejercicio 6 — Crear la vista y las URLs

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej06_1_vscode_vista_item_list.png` | Vista `item_list`: consulta todos los ítems y los envía a la plantilla. |
| `Ej06_2_vscode_core_urls.png` | URLs de la aplicación `core`, enlazadas después en `config/urls.py` con `include()`. |

## Ejercicio 7 — Crear las plantillas

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej07_1_vscode_item_list_html.png` | Plantilla `item_list.html`: hereda de `base.html` y recorre los ítems con `{% for %}` / `{% empty %}`. |
| `Ej07_2_navegador_plantilla_renderizada.png` | La misma plantilla ya procesada por Django y mostrada en el navegador. |

## Ejercicio 8 — Configurar el administrador y cargar datos

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej08_1_vscode_admin_py.png` | Registro del modelo `Item` en el administrador con `list_display`, `search_fields` y `list_filter`. |
| `Ej08_2_navegador_admin_login.png` | Acceso al panel de administración de Django. |
| `Ej08_3_terminal_items_en_bd.png` | Los dos ítems de prueba realmente almacenados en la base de datos, con su id y fecha de creación. |
| **`Ej08_4_admin_lista_items.png`** | **Pendiente: tienes que tomarla tú.** Ver `Ej08_4_FALTA_admin_lista_items.txt`. |

## Ejercicio 9 — Verificar el funcionamiento

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej09_1_terminal_check_y_tests.png` | `manage.py check` sin errores y las 6 pruebas automatizadas superadas. |
| `Ej09_2_navegador_catalogo.png` | Página principal en `http://127.0.0.1:8000/` mostrando el listado de ítems. |
| `Ej09_3_vscode_tests.png` | Pruebas escritas para el modelo `Item` y para la vista `item_list`. |

## Ejercicio 10 — Documentar y subir el proyecto

| Archivo | Pie de foto sugerido |
|---|---|
| `Ej10_1_terminal_requirements_y_git.png` | Dependencias fijadas en `requirements.txt`, historial de commits y árbol de trabajo limpio. |

---

## Carpeta `Renders alternativos\`

Mismo contenido (código y salidas reales) dibujado como terminal: más compacto y
legible, pero **no** son capturas de pantalla. Úsalos solo si prefieres ese formato.
