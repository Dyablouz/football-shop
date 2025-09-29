from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
# class employee(models.Model):
#     nama = models.CharField(max_length=200)
#     umur = models.IntegerField()
#     persona = models.TextField()

# class Book(models.Model):
#     id = models.UUID()
#     title = models.CharField(max_length=255)

# class Author(models):
#     bio = models.TextField()
#     books = models.ManyToManyField(Book)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)