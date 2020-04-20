from django.core.management import BaseCommand

from core.models import Project, Task


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(f'Deleting all ectries in DB'))

        Project.objects.all().delete()
        Task.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'All DB entries are deleted'))