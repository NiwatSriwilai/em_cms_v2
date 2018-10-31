from rest_framework import serializers
from . models import Shop,Category
from rest_framework import viewsets
class CategorySerialiser(serializers.ModelSerializer):
    #shops = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = '__all__'

class ShopSerialiser(serializers.ModelSerializer):
    category = CategorySerialiser(read_only=True)
    class Meta:
        model = Shop
        fields = '__all__'
        #fields = ['pk']

class CategoryWithShopsSerialiser(serializers.ModelSerializer):
    shops = ShopSerialiser(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

