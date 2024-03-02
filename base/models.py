from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    age = models.IntegerField()
    phonenumber = PhoneNumberField(blank=True)
    email=models.EmailField()