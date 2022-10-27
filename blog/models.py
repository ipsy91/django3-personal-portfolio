from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} {self.date}"