from django.urls import path
from .views import *

urlpatterns = [
    path("users/",list_users,name="user-create"),
    path("users/add/",UserAdd.as_view(),name="user-add"),
    path("users/<int:pk>",UserUpdateDelete.as_view(),name="user-update-delete")
]