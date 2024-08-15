from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product, Category, Suppiler
from .serializers import ProductSerializer, CategorySerializer, SuppilerSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products/',
        'GET /api/products/:id'
        'GET /api/categories/',
        'GET /api/categories/:id'
        'GET /api/suppilers/',
        'GET /api/suppilers/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request ,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategory(request, pk):
    categories = Category.objects.get(id=pk)
    serializer = CategorySerializer(categories, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSuppilers(request):
    suppilers = Suppiler.objects.all()
    serializer = SuppilerSerializer(suppilers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSuppiler(request, pk):
    suppilers = Suppiler.objects.get(id=pk)
    serializer = SuppilerSerializer(suppilers, many=False)
    return Response(serializer.data)
