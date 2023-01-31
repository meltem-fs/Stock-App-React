from django.db import models
from django.contrib.auth.models import User

class Firm(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}-{self.stock}'


class Purchases(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True)
    firm = models.ForeignKey(Firm,on_delete=models.PROTECT,null=True)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,null=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.product.name}-{self.quantity}'



class Sales(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,null=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.product.name}-{self.quantity}'