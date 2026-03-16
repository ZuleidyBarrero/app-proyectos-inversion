from django.shortcuts import render


def login_view(request):
    return render(request, "users/login.html")


def user_list(request):
    return render(request, "users/user_list.html")