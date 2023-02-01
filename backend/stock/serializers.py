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

    total_price=serializers.SerializerMethodField()
    category=serializers.SerializerMethodField()
    firm=serializers.StringRelatedField(read_only=True)
    firm_id=serializers.IntegerField()
    brand=serializers.StringRelatedField(read_only=True)
    brand_id=serializers.IntegerField()
    product=serializers.StringRelatedField(read_only=True)
    product_id=serializers.IntegerField()

    class Meta:
        model=Purchases
        fields=("id","user","category","firm","firm_id","brand","brand_id", "product","product_id", "quantity","price","total_price")

    def get_category(self,obj):
        return obj.product.category.name

    def get_total_price(self,obj):
        return obj.quantity*obj.price


class SalesSerializers(serializers.ModelSerializer):

    total_price=serializers.SerializerMethodField()
    category=serializers.SerializerMethodField()
    brand=serializers.StringRelatedField(read_only=True)
    brand_id=serializers.IntegerField()
    product=serializers.StringRelatedField(read_only=True)
    product_id=serializers.IntegerField()

    class Meta:
        model=Sales
        fields=("id","user","category","brand","brand_id", "product","product_id", "quantity","price","total_price")

    def get_category(self,obj):
        return obj.product.category.name    

    def get_total_price(self,obj):
        return obj.quantity*obj.price
    