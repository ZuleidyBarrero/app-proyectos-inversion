# Modelos de la app projects

class Project:
    """
    Modelo conceptual inicial del proyecto de inversión pública.
    Este archivo todavía no usa Django real; por ahora define la estructura base.
    """

    def __init__(
        self,
        nombre,
        sector,
        problema,
        objetivo_general,
        poblacion_objetivo,
        barrio=None,
        vereda=None,
        comuna=None,
        corregimiento=None,
        presupuesto=0,
        estado="Borrador",
        observaciones=""
    ):
        self.nombre = nombre
        self.sector = sector
        self.problema = problema
        self.objetivo_general = objetivo_general
        self.poblacion_objetivo = poblacion_objetivo
        self.barrio = barrio
        self.vereda = vereda
        self.comuna = comuna
        self.corregimiento = corregimiento
        self.presupuesto = presupuesto
        self.estado = estado
        self.observaciones = observaciones