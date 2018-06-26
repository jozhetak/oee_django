from django.db import models
from items.models import Item
from bom.models import Bom
from job_orders_detail.models import JobOrderDetail


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
    item = models.ForeignKey(
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
    def ws(self):
        item_id = self.item.id
        boms = Bom.objects.filter(item_id = item_id)
        for bom in boms:
            return str(bom.workstation_id)

    
    @property
    def item_name(self):
        return self.item.item_name

    @property
    def item_code(self):
        return self.item.item_code
    
    @property
    def job_order_detail_create(self):
        detail_dict = {'job_order':self.id,
                       'item':self.item,
                       'workstation':'',
                       'production_rate':'',
        }
        job_order_detail_entries = JobOrderDetail.objects.filter(job_order = self.id)
        if job_order_detail_entries.exists():
            return True
        else:
            boms = Bom.objects.filter(item_id=self.item)
            if boms:
                for bom in boms:
                    detail_dict['workstation'] = bom.workstation_id
                    detail_dict['production_rate'] = bom.production_rate
                    job_orders_detail = JobOrderDetail(**detail_dict)
                    job_orders_detail.save()
            return True

    def save(self, *args, **kwargs):
        super(JobOrder, self).save(*args, **kwargs)
        self.job_order_detail_create
    

    def __str__(self):
        return "Job No %s %s %s Lote:%s" % (self.job_number, self.item_code, self.item_name, self.batch_number)

    