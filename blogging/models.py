from distutils.command.upload import upload
from django.db import models
from django.db.models import SET_NULL

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True,null=True)
    status = models.BooleanField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    mini_description = models.CharField(max_length=300)
    content = models.TextField
    slug = models.SlugField(max_length=255, unique=True,null=True)
    status = models.BooleanField()
    image = models.ImageField(upload_to='blogging/images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

#for items option in the posts
    def __str__(self):
        return self.title
