from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            if request.user.is_authenticated:
                project.creado_por = request.user
            project.save()
            return redirect("project_detail", project_id=project.id)
    else:
        form = ProjectForm()

    return render(request, "projects/project_form.html", {"form": form})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/project_detail.html", {"project": project})


def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_detail", project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, "projects/project_form.html", {"form": form, "project": project})