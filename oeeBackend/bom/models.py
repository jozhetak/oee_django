from django.db import models
from items.models import Item
from workstations.models import Workstation
# Create your models here.

class Bom(models.Model):
    
    item_id = models.ForeignKey(
        Item,
        related_name='item',
        on_delete=models.CASCADE
    )
    workstation_id = models.ForeignKey(
        Workstation,
        related_name='workstation',
        on_delete=models.CASCADE
    )
    production_rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def bom_str(self, Workstation, Item):
        return str('%d: %s' % (Item.item_name, Workstation.ws_name))

    # def __str__(self):
    #     return self.bom_str(self, Workstation, Item)

    