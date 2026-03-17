from django.shortcuts import render


def forbidden_response(request, message):
    return render(
        request,
        "403.html",
        {"message": message},
        status=403,
    )