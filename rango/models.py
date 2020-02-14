from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# Inherit from Model base class
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    # Primary Key
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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
