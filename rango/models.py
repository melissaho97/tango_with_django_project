from django.db import models

# Create your models here.
# Inherit from Model base class

class Category(models.Model):
    # Primary Key
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    # Change Categorys into Categories
    class Meta:
        verbose_name_plural = 'Categories'

    # without the folowing, it will show as <Category: Category object> if you were to print() the object
    def __str__(self):
        return self.name

class Page(models.Model):
    # Foreign Key
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
