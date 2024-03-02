from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, generics
 
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerialize

class UserAdd(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerialize

@api_view(["GET","POST","PUT"])
def list_users(requests):
    if requests.method == "GET":
        list_user = Users.objects.all()

        serialize = UserSerialize(list_user,many=True)
        return JsonResponse(serialize.data,safe=False)
    
    elif requests.method == "POST":
        data = JSONParser().parse(requests)
        serialize = UserSerialize(data=data)

        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serialize.errors, status=status.HTTP_400_BAD_REQUEST)