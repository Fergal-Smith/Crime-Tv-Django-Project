from django.db import models
from django.contrib.auth.models import User
from shows.models import Show

class Review(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.show.title} - {self.rating}"
