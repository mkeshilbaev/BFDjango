from django.db import models

from utils.validators import validate_file_size

class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='attachments',
                                  validators=[validate_file_size],
                                  null=True, blank=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def top_three(self):
        three = Category.objects.all()[:3]
        return three


class Product(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    attachment = models.FileField(upload_to='attachments',
                                  validators=[validate_file_size],
                                  null=True, blank=True)

    # image = models.ImageField(upload_to='media',
    #                           validators=[validate_file_size],
    #                           null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # abstract = True

    def __str__(self):
        return self.name

    def top_ten(self):
        three = Product.objects.all()[:10]
        return three

    def round_price(self):
        return round(self.price, 2)

    def short_name(self):
        raise NotImplementedError()


# class OnlineProduct(Product):
#     sale = models.CharField(max_length=100)
#     status = models.CharField(max_length=100)
#
#     class Meta:
#         ordering = ('name',)
#
#     def short_name(self):
#         return self.name[:10]
#
#
# class OfflineProduct(Product):
#     address = models.TextField(max_length=200)
#
#     def short_name(self):
#         return self.name[:5]
