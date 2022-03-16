from django.db import models
from django.db.models import CASCADE
from posts.models import Post

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)
