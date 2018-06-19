from django.db import models
from items.models import Item


# Create your models here.

class JobOrder(models.Model):

    JOB_STATUS_CHOICES = (
        ('Created', 'Creada'),
        ('Planned', 'Planificada'),
        ('In_process', 'En proceso'),
        ('Closed', 'Cerrada'),
        ('Canceled', 'Cancelada')
    )

    job_number = models.CharField(max_length=10)
    item_id = models.ForeignKey(
        Item,
        related_name='%(class)s_item',
        on_delete=models.DO_NOTHING
    )
    planned_qty = models.IntegerField(default=1)
    cmplt_qty = models.IntegerField(null=True, blank=True)
    due_date = models.DateField()
    job_status = models.CharField(
        max_length=12,
        choices=JOB_STATUS_CHOICES,
        default='Created'
    )
    start_datetime = models.DateTimeField(null=True, blank=True)
    close_datetime = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    batch_number = models.CharField(max_length=10)

    @property
    def item_name(self):
        return self.item_id.item_name

    @property
    def item_code(self):
        return self.item_id.item_code


    def __str__(self):
        return "Job No %s %s %s Lote:%s" % (self.job_number, self.item_code, self.item_name, self.batch_number)

    