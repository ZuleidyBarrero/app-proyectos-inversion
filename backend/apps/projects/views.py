# Vistas de la app projects

def project_list():
    return {
        "template": "projects/project_list.html",
        "message": "Listado de proyectos"
    }


def project_create():
    return {
        "template": "projects/project_form.html",
        "message": "Formulario para crear proyecto"
    }


def project_detail(project_id):
    return {
        "template": "projects/project_detail.html",
        "message": f"Detalle del proyecto {project_id}"
    }


def project_update(project_id):
    return {
        "template": "projects/project_form.html",
        "message": f"Formulario para editar el proyecto {project_id}"
    }