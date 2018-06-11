from django.db import models

# Create your models here.

class Plant(models.Model):

    plant_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plant_name