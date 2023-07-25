from django.db import models
from django.urls import reverse

class Product(models.Model):
    name    = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='somepictures/')

    def get_absolute_url(self):
        return reverse('save')    

    def __str__(self) -> str:
        return self.name
