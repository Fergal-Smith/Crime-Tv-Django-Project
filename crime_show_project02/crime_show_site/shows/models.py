from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Show(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='shows/', blank=True, null=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg']
