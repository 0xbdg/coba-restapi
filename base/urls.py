from django.urls import path
from .views import *

urlpatterns = [
    path("users/",list_users,name="user-list"),
    path("products/",list_products,name="product-list"),
    path("users/add/",UserAdd.as_view(),name="user-add"),
    path("users/<int:pk>",UserUpdateDelete.as_view(),name="user-update-delete"),
    path("products/add/",ProductAdd.as_view(),name="product-add"),
    path("products/<int:pk>",ProductUpdateDelete.as_view(),name="product-update-delete")
]