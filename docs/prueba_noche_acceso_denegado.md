# Prueba nocturna de acceso denegado

## Objetivo
Verificar que cuando un usuario no tenga permisos, el sistema muestre una página clara de acceso denegado.

## Casos a probar

### Caso 1
Usuario consulta intentando crear proyecto.
Resultado esperado: pantalla de acceso denegado.

### Caso 2
Usuario revisor intentando editar proyecto.
Resultado esperado: pantalla de acceso denegado.

### Caso 3
Usuario formulador intentando cambiar estado.
Resultado esperado: pantalla de acceso denegado.

### Caso 4
Usuario aprobador intentando registrar observación si no tiene rol de revisión.
Resultado esperado: pantalla de acceso denegado.