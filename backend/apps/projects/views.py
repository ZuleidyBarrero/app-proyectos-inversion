from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectAttachmentForm, ProjectForm
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
    attachment_form = ProjectAttachmentForm()
    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
            "attachment_form": attachment_form,
        },
    )


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


def project_attachment_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.project = project
            if request.user.is_authenticated:
                attachment.cargado_por = request.user
            attachment.save()

    return redirect("project_detail", project_id=project.id)