from rest_framework import serializers
from .models import *

class UserSerialize(serializers.ModelSerializer):
    class Meta: 
        model=tbl_users
        fields = ('id','username','age','phonenumber','email')

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = tbl_products
        fields = ['id','nama_produk','tipe','jumlah',"harga"]