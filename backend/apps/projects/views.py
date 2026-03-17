from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectAttachmentForm, ProjectForm, ProjectReviewForm
from .models import Comuna, Corregimiento, Project, ProjectReview, ProjectStatusHistory


def project_list(request):
    projects = Project.objects.select_related(
        "comuna", "barrio", "corregimiento", "vereda", "creado_por"
    ).all()

    q = request.GET.get("q", "").strip()
    estado = request.GET.get("estado", "").strip()
    sector = request.GET.get("sector", "").strip()
    comuna_id = request.GET.get("comuna", "").strip()
    corregimiento_id = request.GET.get("corregimiento", "").strip()

    if q:
        projects = projects.filter(
            Q(nombre__icontains=q)
            | Q(sector__icontains=q)
            | Q(poblacion_objetivo__icontains=q)
            | Q(problema__icontains=q)
        )

    if estado:
        projects = projects.filter(estado=estado)

    if sector:
        projects = projects.filter(sector__icontains=sector)

    if comuna_id:
        projects = projects.filter(comuna_id=comuna_id)

    if corregimiento_id:
        projects = projects.filter(corregimiento_id=corregimiento_id)

    estados = Project.ESTADOS
    comunas = Comuna.objects.all().order_by("nombre")
    corregimientos = Corregimiento.objects.all().order_by("nombre")

    context = {
        "projects": projects,
        "q": q,
        "estado": estado,
        "sector": sector,
        "comuna_id": comuna_id,
        "corregimiento_id": corregimiento_id,
        "estados": estados,
        "comunas": comunas,
        "corregimientos": corregimientos,
    }
    return render(request, "projects/project_list.html", context)


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creado_por = request.user
            project.save()
            messages.success(request, "Proyecto creado correctamente.")
            return redirect("project_detail", project_id=project.id)
    else:
        form = ProjectForm()

    return render(request, "projects/project_form.html", {"form": form})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    attachment_form = ProjectAttachmentForm()
    review_form = ProjectReviewForm()
    estados_disponibles = [estado for estado, _ in Project.ESTADOS if estado != project.estado]

    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
            "attachment_form": attachment_form,
            "review_form": review_form,
            "estados_disponibles": estados_disponibles,
        },
    )


@login_required
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto actualizado correctamente.")
            return redirect("project_detail", project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, "projects/project_form.html", {"form": form, "project": project})


@login_required
def project_attachment_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.project = project
            attachment.cargado_por = request.user
            attachment.save()
            messages.success(request, "Anexo cargado correctamente.")

    return redirect("project_detail", project_id=project.id)


@login_required
def project_archive(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        project.estado = "Archivado"
        project.save()
        messages.success(request, "Proyecto archivado correctamente.")
        return redirect("project_detail", project_id=project.id)

    return render(request, "projects/project_archive_confirm.html", {"project": project})


@login_required
def project_change_status(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        nuevo_estado = request.POST.get("estado", "").strip()
        observacion = request.POST.get("observacion", "").strip()
        estados_validos = [estado for estado, _ in Project.ESTADOS]

        if nuevo_estado in estados_validos:
            estado_anterior = project.estado
            project.estado = nuevo_estado
            project.save()

            ProjectStatusHistory.objects.create(
                project=project,
                estado_anterior=estado_anterior,
                estado_nuevo=nuevo_estado,
                cambiado_por=request.user,
                observacion=observacion,
            )

            messages.success(request, f"Estado actualizado a: {nuevo_estado}.")
        else:
            messages.error(request, "El estado seleccionado no es válido.")

    return redirect("project_detail", project_id=project.id)


@login_required
def project_review_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.creado_por = request.user
            review.save()
            messages.success(request, "Observación registrada correctamente.")

    return redirect("project_detail", project_id=project.id)