# Prueba nocturna de login y acceso

## Casos a validar

### Caso 1
Entrar a /projects/new/ sin iniciar sesión.
Resultado esperado: redirección al login.

### Caso 2
Iniciar sesión con superusuario.
Resultado esperado: ingreso correcto.

### Caso 3
Crear proyecto autenticado.
Resultado esperado: el proyecto guarda el usuario creador.

### Caso 4
Subir anexo autenticado.
Resultado esperado: el anexo guarda el usuario que lo cargó.

### Caso 5
Cerrar sesión.
Resultado esperado: volver al inicio.