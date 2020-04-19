from django.core.management.base import BaseCommand
from datetime import datetime
import random

from core.models import Task


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of products for creation')
        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new products')
        parser.add_argument('-e', '--exp', action='store_true', help='Create Product with expensive price')

    def handle(self, *args, **kwargs):
        # Product.objects.all().delete()
        total = kwargs['total']
        prefix = kwargs.get('prefix')
        expensive = kwargs.get('exp')

        if not prefix:
            prefix = 'AA'

        for i in range(total):
            b = Task.objects.create(title=f'{prefix}_todo {i}',
                                    description=f'todo {i} description',
                                    completed=i % 2 == 0,
                                    created_by_id=1
                                    )
            self.stdout.write(f'Todo {b.id} was created')