# URLs tipo Django de la app projects

urlpatterns = [
    ("", "project_list"),
    ("new/", "project_create"),
    ("<id>/", "project_detail"),
    ("<id>/edit/", "project_update"),
]