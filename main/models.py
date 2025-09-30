import uuid
from django.db import models
from django.contrib.auth.models import User
from django import forms  



class Product(models.Model):
    Category_Choice = [
        ('shoes', 'Shoe'),
        ('jersey', 'Jersey'),
        ('equipment', 'Equipment')
    ]

    name = models.CharField(max_length=255)  
    price = models.IntegerField()  # item price
    description = models.TextField()  # item description
    thumbnail = models.URLField()  # item image URL
    category = models.CharField(max_length=100, choices=Category_Choice)  # item category
    is_featured = models.BooleanField(default=False)  # featured status
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.category}"




