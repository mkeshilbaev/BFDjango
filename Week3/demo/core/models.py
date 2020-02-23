from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name')

        def __str__(self):
            return f'name: {self.name}'

