from django.db import models
from django.db.models import SET_NULL
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.BooleanField()
    image = models.ImageField(upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL,null=True)

#for items option in the posts
    def __str__(self):
        return self.title