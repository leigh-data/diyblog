from django.db import models
from django.contrib.auth import get_user_model

from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=126)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="posts")
    description = models.TextField()

    class Meta:
        permissions = (('blogger', 'can publish a post'),)
        ordering = ['-created']

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.commenter}|{self.post}"
