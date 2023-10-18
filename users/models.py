from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.CharField(max_length=255, default='Your Default Author')
    title = models.CharField(max_length=255)
    content = models.TextField()
