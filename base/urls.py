from django.urls import path
from .views import *

urlpatterns = [
    path("users/",UserCreate.as_view(),name="user-create"),
    path("user/<int:pk>",UserUpdateDelete.as_view(),name="user-update-delete")
]