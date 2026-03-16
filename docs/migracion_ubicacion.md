# Migración de lógica de ubicación desde PySide6

## Origen
La aplicación de escritorio manejaba parámetros como:
- barrios
- veredas
- barrio_to_comuna
- vereda_to_correg

## Objetivo en la web
Transformar esa lógica en:
- modelos de datos
- relaciones entre entidades geográficas
- validaciones
- selección dinámica en formularios web

## Estrategia inicial
1. Definir modelos conceptuales: Barrio, Vereda, Comuna, Corregimiento
2. Asociar barrio con comuna
3. Asociar vereda con corregimiento
4. Permitir que Project use esas relaciones
5. Más adelante convertir esto en tablas reales de base de datos