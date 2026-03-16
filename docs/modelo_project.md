# Modelo inicial Project

## Propósito
Representar la información básica de un proyecto de inversión pública dentro del sistema web.

## Campos iniciales

- nombre: nombre del proyecto
- sector: sector al que pertenece el proyecto
- problema: descripción del problema identificado
- objetivo_general: propósito principal del proyecto
- poblacion_objetivo: población beneficiaria
- barrio: barrio asociado, si aplica
- vereda: vereda asociada, si aplica
- comuna: comuna asociada, si aplica
- corregimiento: corregimiento asociado, si aplica
- presupuesto: valor estimado del proyecto
- estado: estado del proyecto (por defecto: Borrador)
- observaciones: notas adicionales

## Estados iniciales sugeridos
- Borrador
- En revisión
- Aprobado
- Rechazado
- Archivado
## Modelos geográficos relacionados

### Comuna
Representa una división urbana del municipio.

### Corregimiento
Representa una división rural principal del municipio.

### Barrio
Representa una unidad territorial urbana y puede pertenecer a una comuna.

### Vereda
Representa una unidad territorial rural y puede pertenecer a un corregimiento.

## Relaciones iniciales
- Un barrio puede pertenecer a una comuna
- Una vereda puede pertenecer a un corregimiento
- Un proyecto puede asociarse a barrio o vereda según su ubicación