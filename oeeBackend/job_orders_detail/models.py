from django.db import models
from items.models import Item
from workstations.models import Workstation
from bom.models import Bom



# Create your models here.

class JobOrderDetail(models.Model):

    job_order = models.IntegerField(blank=True, null=True, editable=False)

    # Otros campos

    item = models.ForeignKey(
        Item,
        related_name='%(class)s_item',
        editable=False,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )

    workstation = models.ForeignKey(
        Workstation,
        related_name='%(class)s_workstation',
        editable=False,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )

    production_rate = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.job_order)

    