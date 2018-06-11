from django.db import models
from items.models import Item

# Create your models here.

class Bom(models.Model):

    job_number = models.CharField(max_length=10)
    
    item_id = models.ForeignKey(
        Item,
        related_name='item',
        on_delete=models.DO_NOTHING
    )
    production_rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def item_name(self):
        return self.item_id.item_name

    @property
    def ws_name(self):
        return self.workstation_id.ws_name

    def __str__(self):
        return 'La tasa de producciòn para el Item %s en la workstation %s ha sido añadida' % (self.item_name, self.ws_name)

    