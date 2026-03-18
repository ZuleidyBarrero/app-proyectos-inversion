# Prueba nocturna de menú por rol

## Objetivo
Verificar que el menú superior cambie según el usuario autenticado.

## Casos a probar

### Usuario no autenticado
- debe ver Inicio
- debe ver Iniciar sesión

### Formulador
- debe ver Inicio
- debe ver Proyectos
- debe ver Nuevo proyecto
- debe ver Cerrar sesión

### Revisor
- debe ver Inicio
- debe ver Proyectos
- no debe ver Nuevo proyecto
- debe ver Cerrar sesión

### Aprobador
- debe ver Inicio
- debe ver Proyectos
- no debe ver Nuevo proyecto
- debe ver Cerrar sesión

### Superusuario
- debe ver Inicio
- debe ver Proyectos
- debe ver Nuevo proyecto
- debe ver Usuarios
- debe ver Admin
- debe ver Cerrar sesión