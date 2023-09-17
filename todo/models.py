from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    '''Model for tasks'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True  )
    title = models.CharField(max_length=255)
    deadline = models.DateField()
    tag = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
