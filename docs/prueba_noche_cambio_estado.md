# Prueba nocturna de cambio de estado

## Objetivo
Verificar que un proyecto pueda cambiar entre estados de forma controlada desde su detalle.

## Casos a probar

### Caso 1
Abrir el detalle de un proyecto.
Resultado esperado: ver el formulario de cambio de estado.

### Caso 2
Cambiar de Borrador a En revisión.
Resultado esperado: actualización correcta y mensaje de éxito.

### Caso 3
Cambiar de En revisión a Aprobado.
Resultado esperado: actualización correcta y visible en detalle y listado.

### Caso 4
Cambiar a Rechazado o Archivado.
Resultado esperado: actualización correcta.

### Caso 5
Verificar en el listado.
Resultado esperado: el filtro por estado refleje los cambios realizados.