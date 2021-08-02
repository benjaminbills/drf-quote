from django.db import models

# Create your models here.
class Quote(models.Model):
  author = models.CharField(max_length=30)
  content = models.CharField(max_length=2000)

  def __str__(self):
    return self.author
