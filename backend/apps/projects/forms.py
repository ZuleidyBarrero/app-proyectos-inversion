# Formularios de la app projects

class ProjectForm:
    """
    Formulario conceptual inicial para capturar datos del proyecto.
    """

    campos = [
        "nombre",
        "sector",
        "problema",
        "objetivo_general",
        "poblacion_objetivo",
        "barrio",
        "comuna",
        "vereda",
        "corregimiento",
        "presupuesto",
        "estado",
        "observaciones",
        "anexos",
    ]

    estados_disponibles = [
        "Borrador",
        "En revisión",
        "Aprobado",
        "Rechazado",
        "Archivado",
    ]