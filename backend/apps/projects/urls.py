from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("new/", views.project_create, name="project_create"),
    path("<int:project_id>/", views.project_detail, name="project_detail"),
    path("<int:project_id>/edit/", views.project_update, name="project_update"),
    path("<int:project_id>/archive/", views.project_archive, name="project_archive"),
    path("<int:project_id>/change-status/", views.project_change_status, name="project_change_status"),
    path("<int:project_id>/attachments/new/", views.project_attachment_create, name="project_attachment_create"),
    path("<int:project_id>/reviews/new/", views.project_review_create, name="project_review_create"),
    path("ajax/barrios/", views.barrios_by_comuna, name="barrios_by_comuna"),
    path("ajax/veredas/", views.veredas_by_corregimiento, name="veredas_by_corregimiento"),
]