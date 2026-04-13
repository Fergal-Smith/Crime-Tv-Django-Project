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
        return self.rating_set.aggregate(Avg('score'))['score__avg']

class Rating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} rated {self.show} {self.score}'