from django.db import models

# Create your models here.

class Tache(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    createdDate = models.DateField(auto_now_add=True)
    closed = models.Field(default=False)

    def __srt__(self):
        return self.name + " " + self.description
