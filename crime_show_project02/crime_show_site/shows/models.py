from django.db import models
from django.contrib.auth.models import User  # Needed for Rating.user

class Show(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Rating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)  # References Show
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} rated {self.show} {self.score}'
