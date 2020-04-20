from django.core.management.base import BaseCommand
from django.db.models import Avg, Max, Min
from onlineshop.models import Product


class Command(BaseCommand):
    help = 'see existing products price'

    def handle(self, *args, **kwargs):
        data = [
            Product.objects.aggregate(Avg('price')),
            Product.objects.aggregate(Max('price')),
            Product.objects.aggregate(Min('price')),
        ]
        self.stdout.write(self.style.SUCCESS(data))