from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('products/<str:pk>/', views.getProduct),
    path('categories/', views.getCategories),
    path('categories/<str:pk>/', views.getCategory),
    path('suppilers/', views.getSuppilers),
    path('suppilers/<str:pk>/', views.getSuppiler),
]
