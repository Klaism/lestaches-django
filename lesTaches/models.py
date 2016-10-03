from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField()
    createdDate = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    def __srt__(self):
        return self.name + " " + self.description
