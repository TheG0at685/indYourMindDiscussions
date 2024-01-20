from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    """A new thread that contains a title, info, and comments"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.text
    
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "comments"
    def __str__(self):
        return f"{self.text[:50]}..."