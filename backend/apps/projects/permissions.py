def user_in_group(user, group_name):
    return user.is_authenticated and user.groups.filter(name=group_name).exists()


def can_create_project(user):
    return user.is_superuser or user_in_group(user, "Formulador")


def can_edit_project(user):
    return user.is_superuser or user_in_group(user, "Formulador")


def can_review_project(user):
    return user.is_superuser or user_in_group(user, "Revisor")


def can_change_project_status(user):
    return user.is_superuser or user_in_group(user, "Aprobador")


def can_view_projects(user):
    return user.is_authenticated