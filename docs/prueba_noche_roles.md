# Prueba nocturna de roles y permisos

## Objetivo
Verificar que las acciones del sistema se muestren o bloqueen según el rol del usuario.

## Grupos esperados
- Formulador
- Revisor
- Aprobador
- Consulta

## Casos a probar

### Caso 1
Usuario Formulador
- puede crear proyectos
- puede editar proyectos
- puede cargar anexos
- no puede cambiar estado
- no puede registrar observaciones de revisión

### Caso 2
Usuario Revisor
- puede ver proyectos
- puede registrar observaciones
- no puede editar proyectos
- no puede cambiar estado

### Caso 3
Usuario Aprobador
- puede ver proyectos
- puede cambiar estado
- puede archivar
- no necesariamente edita el contenido técnico

### Caso 4
Usuario Consulta
- solo puede visualizar