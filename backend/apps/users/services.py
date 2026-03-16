# Servicios conceptuales de la app users

ROLES_VALIDOS = [
    "Administrador",
    "Formulador",
    "Revisor",
    "Consulta",
]


def role_valido(role):
    return role in ROLES_VALIDOS


def usuario_activo(user):
    return getattr(user, "activo", False) is True