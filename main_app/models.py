from django.db import models
from django.urls import reverse

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
