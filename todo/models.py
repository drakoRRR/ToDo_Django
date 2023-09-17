from django.db import models

# Create your models here.
class Task(models.Model):
    '''Model for tasks'''
    title = models.CharField(max_length=255)
    deadline = models.DateField()
    tag = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
