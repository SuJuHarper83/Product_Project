from django.urls import path
from . import views

urlpatters = [
    path('', views.products_list),
]