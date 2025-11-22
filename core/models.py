from django.db import models

# Create your models here.
class Composer(models.Model):
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Music(models.Model):
    title = models.CharField(max_length=250)
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} by {self.composer}"