from django.db import models

# Create your models here.
class Subway(models.Model):
  title = models.CharField(max_length = 200)
  location = models.TextField()

  def __str__(self):
    return self.title