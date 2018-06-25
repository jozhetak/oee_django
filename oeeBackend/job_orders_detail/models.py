from django.db import models
from job_orders.models import JobOrder
from items.models import Item
from workstations.models import Workstation
from bom.models import Bom



# Create your models here.

class JobOrderDetail(models.Model):

    JOB_DETAIL_STATUS_CHOICES = (
        ('Created', 'Creada'),
        ('Planned', 'Planificada'),
        ('In_process', 'En proceso'),
        ('Closed', 'Cerrada'),
        ('Canceled', 'Cancelada')
    )

    job_order = models.ForeignKey(
        JobOrder,
        related_name='%(class)s_job_order',
        on_delete=models.DO_NOTHING
    )

    job_detail_status = models.CharField(
        max_length=12,
        choices=JOB_DETAIL_STATUS_CHOICES,
        default='In_process'
    )

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
        return 'JOb order deatil_'+ self.job_order

    