from django.db import models
from django.contrib.auth.models import User

class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relasi ke user
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.title