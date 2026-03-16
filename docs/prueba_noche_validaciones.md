# Prueba nocturna de validaciones de ubicación

## Casos a probar

### Caso 1
Intentar guardar un proyecto sin ubicación.
Resultado esperado: error de validación.

### Caso 2
Seleccionar barrio sin comuna.
Resultado esperado: error de validación.

### Caso 3
Seleccionar vereda sin corregimiento.
Resultado esperado: error de validación.

### Caso 4
Seleccionar comuna y barrio correctos.
Resultado esperado: guardar correctamente.

### Caso 5
Seleccionar corregimiento y vereda correctos.
Resultado esperado: guardar correctamente.

### Caso 6
Seleccionar ubicación urbana y rural al mismo tiempo.
Resultado esperado: error de validación.