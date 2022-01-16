from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)
    suppliers = models.OneToOneField('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    first_name = models.CharField(max_length=40)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}'


class Towar(models.Model):
    product_name = models.CharField(max_length=40)
    clients = models.ManyToManyField('Client')

    def __str__(self):
        return f'{self.product_name}'


class Supplier(models.Model):
    products_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.products_name}'
