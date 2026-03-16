# Modelos conceptuales de la app projects

class Comuna:
    def __init__(self, nombre):
        self.nombre = nombre


class Corregimiento:
    def __init__(self, nombre):
        self.nombre = nombre


class Barrio:
    def __init__(self, nombre, comuna=None):
        self.nombre = nombre
        self.comuna = comuna


class Vereda:
    def __init__(self, nombre, corregimiento=None):
        self.nombre = nombre
        self.corregimiento = corregimiento


class Project:
    """
    Modelo conceptual inicial del proyecto de inversión pública.
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