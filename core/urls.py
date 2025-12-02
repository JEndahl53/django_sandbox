# django_sandbox/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_page, name='search_page'),
    path('counter/', views.counter, name='counter'),
    path('search/composers', views.search_composers, name='search_composers'),
]
