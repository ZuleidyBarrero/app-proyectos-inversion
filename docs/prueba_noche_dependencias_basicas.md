# Prueba nocturna de dependencias básicas de ubicación

## Objetivo
Verificar que el formulario cargue barrios y veredas de forma coherente según la selección y el contexto del formulario.

## Casos a revisar

### Caso 1
Editar un proyecto urbano existente.
Resultado esperado: se vean la comuna y el barrio correctos.

### Caso 2
Editar un proyecto rural existente.
Resultado esperado: se vean el corregimiento y la vereda correctos.

### Caso 3
Enviar formulario con error de validación.
Resultado esperado: que el formulario conserve la comuna/corregimiento seleccionados y filtre barrios/veredas correctamente.

## Observación
Esta es una dependencia básica del lado del servidor. Más adelante se puede mejorar con JavaScript dinámico.