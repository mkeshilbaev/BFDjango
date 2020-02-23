from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    num_pages = models.FloatField(default=0)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='books')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name='books')