# Servicios de la app projects
# Servicios de la app projects

def validar_presupuesto(presupuesto):
    return presupuesto >= 0


def validar_ubicacion(barrio=None, vereda=None):
    return barrio is not None or vereda is not None


def estado_inicial():
    return "Borrador"