"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ContactsView, ProductsListView, ProductView, product

app_name = 'catalog'  # Устанавливаем пространство имен для приложения

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),  # URL для списка продуктов
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),  # URL для отдельного продукта
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('custom_product/<int:pk>/', product, name='custom_product_view'),
]
