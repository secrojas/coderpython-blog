from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.BooleanField()

#for items option in the posts
    def __str__(self):
        return self.title
