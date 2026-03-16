from django.shortcuts import render


def project_list(request):
    return render(request, "projects/project_list.html")


def project_create(request):
    return render(request, "projects/project_form.html")


def project_detail(request, project_id):
    return render(request, "projects/project_detail.html", {"project_id": project_id})


def project_update(request, project_id):
    return render(request, "projects/project_form.html", {"project_id": project_id})