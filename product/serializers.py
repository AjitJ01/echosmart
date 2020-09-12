from rest_framework import serializers
from product.models import Product
from product.models import Category
from product.models import Inventory




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image')


class ProductSerializer(serializers.ModelSerializer):

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category')

    class Meta:
        model = Product
        fields = ('id', 'category_id', 'name', 'brand', 'description', 'price', 'unit_of_measure', 'image')


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('id', 'product_id', 'quantity')