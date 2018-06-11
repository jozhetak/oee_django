from django.db import models
from plants.models import Plant 
# Create your models here.

class Workstation(models.Model):
    WS_TYPE_CHOICES = (
        ('FA', 'Fabricación'),
        ('EN', 'Envasado'),
        ('ET', 'Etiquetado')
    )

    ws_name = models.CharField(max_length=256)
    ws_type = models.CharField(
        max_length=6, 
        choices=WS_TYPE_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    ws_plant = models.ForeignKey(
        Plant,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='plant'
    )

    def __str__(self):
        return self.ws_name