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
from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, published_toggle, view_all

app_name = BlogConfig.name

urlpatterns = [
    path('create', PostCreateView.as_view(), name='create'),
    path('', PostListView.as_view(), name='list'),
    path('view_all', view_all, name='view_all'),
    path('view/<int:pk>', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('published/<int:pk>', published_toggle, name='published_toggle'),
]