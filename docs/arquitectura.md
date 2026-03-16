# Arquitectura inicial del sistema

## Objetivo
Construir una aplicación web para la formulación y gestión de proyectos de inversión pública.

## Estructura inicial

- backend/core: configuración principal
- backend/apps: aplicaciones del sistema
- backend/templates: páginas HTML
- backend/static: archivos estáticos
- backend/media: archivos cargados por usuarios
- docs: documentación funcional y técnica

## Primera app
projects

## Funcionalidades iniciales esperadas
- Inicio de sesión
- Crear proyecto
- Editar proyecto
- Listar proyectos
- Cargar anexos
- Gestión de catálogos geográficos
## Nueva app conceptual
users

## Propósito de la app users
Gestionar autenticación, usuarios y roles del sistema.
## Módulo core

Responsable de la navegación general del sistema.

Incluye:

- home
- rutas principales
- conexión entre apps
## Estructura tipo Django preparada

Se crean los siguientes componentes base:

- backend/manage.py
- backend/core/settings.py
- backend/core/wsgi.py
- backend/core/asgi.py

Además, cada app empieza a adoptar estructura similar a Django:

- apps.py
- admin.py
- tests.py
- urls_real.py