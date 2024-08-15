from rest_framework.serializers import ModelSerializer
from base.models import Product, Suppiler, Category

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class SuppilerSerializer(ModelSerializer):
    class Meta:
        model = Suppiler
        fields = '__all__'