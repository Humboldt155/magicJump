from django.db import models

class Department(models.Model):
    id = models.CharField(max_length=2, primary_key=True, unique=True)
    name = models.CharField(max_length=200)

class Model(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=200)

class Product(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    avs = models.DateField(default='2099-12-31')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='99')

class Attribute(models.Model):
    id = models.CharField(max_length=9, primary_key=True, unique=True)
    name = models.CharField(max_length=200)

class Value(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
