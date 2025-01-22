# posts/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    #slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_published = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.text[:50]

    class Meta:
        ordering = ["-text"]