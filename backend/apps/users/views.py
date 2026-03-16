# Vistas conceptuales de la app users

def login_view():
    return {
        "template": "users/login.html",
        "message": "Formulario de inicio de sesión"
    }


def user_list():
    return {
        "template": "users/user_list.html",
        "message": "Listado de usuarios"
    }