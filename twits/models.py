from django.db import models
from accounts.models import UserData


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text[:10]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content[:10]
