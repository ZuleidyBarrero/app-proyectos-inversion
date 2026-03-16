from django.contrib.auth import authenticate, login, logout
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


def user_list(request):
    return render(request, "users/user_list.html")