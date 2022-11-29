from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.

class Post(models.Model):
    body = MarkdownxField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.title
