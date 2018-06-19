from django.db import models
from items.models import Item
from workstations.models import Workstation
# Create your models here.

class Bom(models.Model):
    
    item_id = models.ForeignKey(
        Item,
        related_name='%(class)s_item',
        on_delete=models.CASCADE
    )
    workstation_id = models.ForeignKey(
        Workstation,
        related_name='%(class)s_workstation',
        on_delete=models.CASCADE
    )
    production_rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # def bom_str(self, *args):
    #     return str('%s: %s' % (Item.item_name, Workstation.ws_name))

    @property
    def item_name(self):
        return self.item_id.item_name

    @property
    def ws_name(self):
        return self.workstation_id.ws_name

    def __str__(self):
        return 'La tasa de producciòn para el Item %s en la workstation %s ha sido añadida' % (self.item_name, self.ws_name)

    