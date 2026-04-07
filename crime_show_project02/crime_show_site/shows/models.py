from django.db import models
from django.urls import reverse

class Show(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='shows/', default='placeholder.png')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_detail', kwargs={'pk': self.pk})
