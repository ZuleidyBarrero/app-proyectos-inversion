def user_in_group(user, group_name):
    return user.is_authenticated and user.groups.filter(name=group_name).exists()


def build_menu_for_user(user):
    menu = [
        {"label": "Inicio", "url": "/"},
        {"label": "Ayuda", "url": "/users/help/"},
    ]

    if not user.is_authenticated:
        menu.append({"label": "Iniciar sesión", "url": "/users/login/"})
        return menu

    if user.is_superuser:
        menu.extend([
            {"label": "Proyectos", "url": "/projects/"},
            {"label": "Nuevo proyecto", "url": "/projects/new/"},
            {"label": "Documentos", "url": "/projects/documents/"},
            {"label": "Usuarios", "url": "/users/"},
            {"label": "Perfil", "url": "/users/profile/"},
            {"label": "Admin", "url": "/admin/"},
            {"label": "Cerrar sesión", "url": "/users/logout/"},
        ])
        return menu

    menu.append({"label": "Proyectos", "url": "/projects/"})
    menu.append({"label": "Documentos", "url": "/projects/documents/"})

    if user_in_group(user, "Formulador"):
        menu.append({"label": "Nuevo proyecto", "url": "/projects/new/"})

    menu.append({"label": "Perfil", "url": "/users/profile/"})
    menu.append({"label": "Cerrar sesión", "url": "/users/logout/"})
    return menu