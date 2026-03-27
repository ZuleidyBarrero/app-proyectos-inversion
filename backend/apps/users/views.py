from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/projects/")
        else:
            error = "Usuario o contraseña incorrectos."

    return render(request, "users/login.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def user_list(request):
    return render(request, "users/user_list.html")


@login_required
def profile_view(request):
    grupos = request.user.groups.all()

    accesos = {
        "puede_crear": request.user.is_superuser or grupos.filter(name="Formulador").exists(),
        "puede_revisar": request.user.is_superuser or grupos.filter(name="Revisor").exists(),
        "puede_aprobar": request.user.is_superuser or grupos.filter(name="Aprobador").exists(),
        "puede_consultar": request.user.is_authenticated,
        "es_superusuario": request.user.is_superuser,
    }

    return render(
        request,
        "users/profile.html",
        {
            "grupos": grupos,
            "accesos": accesos,
        },
    )
def help_view(request):
    return render(request, "users/help.html")