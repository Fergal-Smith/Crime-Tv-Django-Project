from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Show(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='shows/', default='placeholder.png')
    
    def __str__(self):
        return f"{self.user.username} - {self.show.title}: {self.stars}"
        
class Rating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_detail', kwargs={'pk': self.pk})
        
class Show(models.Model):

    def update_average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            self.average_rating = sum(r.stars for r in ratings) / ratings.count()
        else:
            self.average_rating = 0
        self.save()
