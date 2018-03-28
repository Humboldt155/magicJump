from django.db import models

# Create your models here.
class Model(models.Model):
    modelId = models.CharField(max_length=10)
    modelName = models.CharField(max_length=200)

# Create your models here.
class Product(models.Model):
    productId = models.CharField(max_length=8)
    productName = models.CharField(max_length=200)
    modelId = models.ForeignKey(Model, on_delete=models.CASCADE)
    
class Attribute(models.Model):
    attributeId = models.CharField(max_length=9)
    attributeName = models.CharField(max_length=200)
    