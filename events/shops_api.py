from rest_framework import serializers
from . models import Shop,Category
from rest_framework import viewsets
class ShopSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('id')
class ShopViewSet(viewsets.ModelViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerialiser

class CategorySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
