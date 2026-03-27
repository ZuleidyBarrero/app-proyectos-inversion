# Prueba nocturna de perfil de usuario

## Objetivo
Verificar que cada usuario vea su información y accesos según el rol asignado.

## Casos a probar

### Caso 1
Ingresar con formulador1.
Resultado esperado: ver grupo Formulador y permiso de crear proyectos.

### Caso 2
Ingresar con revisor1.
Resultado esperado: ver grupo Revisor y permiso de registrar observaciones.

### Caso 3
Ingresar con aprobador1.
Resultado esperado: ver grupo Aprobador y permiso de cambiar estado.

### Caso 4
Ingresar con consulta1.
Resultado esperado: ver grupo Consulta y solo acceso de visualización.

### Caso 5
Ingresar con superusuario.
Resultado esperado: ver acceso total y opción Admin en el menú.