from .menu import build_menu_for_user


def menu_context(request):
    return {
        "main_menu": build_menu_for_user(request.user)
    }