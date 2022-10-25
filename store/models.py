    from django.db import models

from .base_model import BaseModel
from django.contrib.auth.models import User

# Create your models here.

TRANSACTION_STATUS = [
    ('success', 'Success'),
    ('pending', 'Pending'),
    ('failed', 'Failed'),
]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    desc = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, related_name="product_orders", on_delete=models.SET_NULL, null=True)
    transaction = models.OneToOneField("Transaction", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name="cutomer_orders", on_delete=models.CASCADE)
    order_ref = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.order_ref

class Transaction(models.Model):
    amount = models.FloatField()
    reference = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, default="pending", choices=TRANSACTION_STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.reference)

