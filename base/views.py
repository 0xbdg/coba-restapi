from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerialize

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerialize
