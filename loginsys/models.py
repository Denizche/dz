# Create your models here.

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=30)
    users = models.ManyToManyField(User, through='UserService')
    price = models.IntegerField(default=500)
    picture = models.ImageField(default='order/images/333.png', upload_to='order/images')

    def __str__(self):
        return self.title


class UserService(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="no desc")
    desc_picture = models.ImageField(default='order/images/333.png', upload_to='order/images')
