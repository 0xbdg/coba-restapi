from rest_framework import serializers
from .models import Users

class UserSerialize(serializers.ModelSerializer):
    class Meta: 
        model=Users
        fields = ('id','username','phonenumber','age','email')