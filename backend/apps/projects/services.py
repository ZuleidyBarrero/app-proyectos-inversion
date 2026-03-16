# Servicios de la app projects

ESTADOS_VALIDOS = [
    "Borrador",
    "En revisión",
    "Aprobado",
    "Rechazado",
    "Archivado",
]


def validar_presupuesto(presupuesto):
    return presupuesto >= 0


def validar_ubicacion(barrio=None, vereda=None):
    return barrio is not None or vereda is not None


def estado_inicial():
    return "Borrador"


def estado_valido(estado):
    return estado in ESTADOS_VALIDOS


def obtener_comuna_desde_barrio(barrio):
    if barrio and hasattr(barrio, "comuna"):
        return barrio.comuna
    return None


def obtener_corregimiento_desde_vereda(vereda):
    if vereda and hasattr(vereda, "corregimiento"):
        return vereda.corregimiento
    return None