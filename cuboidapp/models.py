from django.db import models
from django.contrib.auth.models import User

class Box(models.Model):
    length = models.FloatField()
    breadth = models.FloatField()
    height = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boxes_created')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)