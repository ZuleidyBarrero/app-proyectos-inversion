# Prueba nocturna de historial de estados

## Objetivo
Verificar que cada cambio de estado quede registrado con trazabilidad.

## Casos a probar

### Caso 1
Abrir un proyecto y cambiar su estado.
Resultado esperado: se actualiza el estado actual.

### Caso 2
Agregar una observación al cambio.
Resultado esperado: la observación aparece en el historial.

### Caso 3
Revisar el detalle del proyecto.
Resultado esperado: se vea el historial con fecha, usuario, estado anterior y estado nuevo.

### Caso 4
Revisar en admin.
Resultado esperado: el historial esté disponible y asociado al proyecto.