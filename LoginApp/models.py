from django.db import models

# Create your models here.
class user (models.Model):
    mail = models.EmailField(max_length=254)
    psw = models.TextField()
    username = models.CharField(max_length=50)
    address = models.TextField()
