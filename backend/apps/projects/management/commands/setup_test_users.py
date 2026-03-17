from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User


class Command(BaseCommand):
    help = "Crea usuarios de prueba y los asigna a grupos base"

    def handle(self, *args, **options):
        users_config = [
            {"username": "formulador1", "email": "formulador1@example.com", "password": "Temporal123*", "group": "Formulador"},
            {"username": "revisor1", "email": "revisor1@example.com", "password": "Temporal123*", "group": "Revisor"},
            {"username": "aprobador1", "email": "aprobador1@example.com", "password": "Temporal123*", "group": "Aprobador"},
            {"username": "consulta1", "email": "consulta1@example.com", "password": "Temporal123*", "group": "Consulta"},
        ]

        for item in users_config:
            user, created = User.objects.get_or_create(
                username=item["username"],
                defaults={"email": item["email"]},
            )

            if created:
                user.set_password(item["password"])
                user.save()

            group, _ = Group.objects.get_or_create(name=item["group"])
            user.groups.clear()
            user.groups.add(group)

        self.stdout.write(self.style.SUCCESS("Usuarios de prueba creados y asignados correctamente."))