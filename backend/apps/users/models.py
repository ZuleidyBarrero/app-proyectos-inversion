# Modelos conceptuales de la app users

class Role:
    def __init__(self, nombre):
        self.nombre = nombre


class User:
    def __init__(self, username, email, password, role=None, activo=True):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.activo = activo