# Estructura geográfica inicial del sistema

## Objetivo
Permitir que los proyectos de inversión pública se registren con ubicación urbana o rural.

## Componentes

### Urbana
- Comuna
- Barrio

Relación:
- Un barrio puede pertenecer a una comuna

### Rural
- Corregimiento
- Vereda

Relación:
- Una vereda puede pertenecer a un corregimiento

## Uso en el sistema
Cuando el usuario registre un proyecto, podrá asociarlo a:
- barrio y comuna, si aplica a zona urbana
- vereda y corregimiento, si aplica a zona rural

## Futuro esperado
- Catálogos cargados desde base de datos
- Listas desplegables dependientes
- Validación de consistencia territorial