# Migración desde aplicación de escritorio PySide6

## Objetivo
Transformar el formulario y la lógica actual de escritorio en una aplicación web.

## Elementos identificados para migrar
- ProjectFormDialog
- Campos de texto
- Listas desplegables
- Campos numéricos
- Área de observaciones
- Carga de archivos
- Validaciones
- Relaciones geográficas: barrios, veredas, comunas, corregimientos

## Estrategia
1. Separar la lógica de negocio de la interfaz.
2. Crear modelos de datos.
3. Crear formularios web.
4. Crear vistas para crear, editar y consultar proyectos.
5. Incorporar autenticación.
6. Incorporar almacenamiento de archivos.