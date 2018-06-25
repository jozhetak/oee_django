from django.db import models
from items.models import Item
from bom.models import Bom


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

    # @property
    # def get_bom_data(self):
    #     boms = Bom.objects.filter(item_id=self.item)
    #     if boms:
    #         for bom in boms:
    #             ws_id = workstation
    #     return ws_id

    # @property
    # def get_(self):
    #     q_issues = self.jobqualityissue_q_issue.filter(reworked=True)
    #     reworked_qty = 0
    #     for q_issue in q_issues:
    #         reworked_qty = reworked_qty + q_issue.q_issue_qty
    #     return reworked_qty


    def __str__(self):
        return "Job No %s %s %s Lote:%s" % (self.job_number, self.item_code, self.item_name, self.batch_number)

    