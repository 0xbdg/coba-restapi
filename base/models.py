from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class tbl_users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    age = models.IntegerField()
    phonenumber = PhoneNumberField(blank=True)
    email=models.EmailField()

class tbl_products(models.Model):
    id = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=100)
    tipe = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    harga = models.CharField(max_length=255)