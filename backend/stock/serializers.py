from rest_framework import serializers
from .models import Firm,Category,Brand,Product,Purchases,Sales


class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model=Firm
        fields="__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=("name","id")


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model=Brand
        fields=("name","id")


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=("name","id","category","brand","stock")


class PurchasesSerializers(serializers.ModelSerializer):

    class Meta:
        model=Purchases
        fields=("id","user","firm","brand","product","quantity","price")


class SalesSerializers(serializers.ModelSerializer):

    class Meta:
        model=Sales
        fields=("id","user","brand","product","quantity","price")