from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Purchases, Sales

@receiver(post_save, sender=Purchases)
def increase_product(sender,instance,created, **kwargs):
    if created:
        quantity = instance.quantity
        prd_id= instance.product.id
        current_product=Product.objects.get(id=prd_id)
        # print(current_product.stock)
        current_product.stock+=quantity
        current_product.save()


@receiver(post_save, sender=Sales)
def increase_product(sender,instance,created, **kwargs):
    if created:
        quantity = instance.quantity
        prd_id= instance.product.id
        current_product=Product.objects.get(id=prd_id)
        # print(current_product.stock)
        current_product.stock-=quantity
        current_product.save()