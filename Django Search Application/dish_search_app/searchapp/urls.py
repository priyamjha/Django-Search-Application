from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_dish, name='search_dish'),
]
