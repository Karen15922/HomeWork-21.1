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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Импортируйте модуль admin
from django.contrib import admin

urlpatterns = [
    path('', include('catalog.urls')),  # Подключить URL-маршруты из приложения catalog для корневого пути
    path('admin/', admin.site.urls),  # URL-маршрут для административной панели Django
    path('catalog/', include('catalog.urls', namespace='catalog')),  # URL-маршруты для приложения catalog
    path('blog/', include('blog.urls', namespace='blog')),  # URL-маршруты для приложения blog
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
