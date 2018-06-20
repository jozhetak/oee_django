from django.db import models
from job_orders.models import JobOrder
from shifts.models import Shift


# Create your models here.

class JobOrderData(models.Model):

    JOB_PARTIAL_STATUS_CHOICES = (
        ('In_process', 'En proceso'),
        ('Closed', 'Cerrada'),
    )

    job_number_id = models.ForeignKey(
        JobOrder,
        related_name='%(class)s_job_order',
        on_delete=models.DO_NOTHING
    )
    shift_id = models.ForeignKey(
        Shift,
        related_name='%(class)s_shift',
        on_delete=models.DO_NOTHING
    )
    job_partial_status = models.CharField(
        max_length=12,
        choices=JOB_PARTIAL_STATUS_CHOICES,
        default='In_process'
    )

    # Cantidades

    packaged_qty = models.IntegerField(null=True, blank=True)
    retention_samples_qty = models.IntegerField(null=True, blank=True)
    reworked_qty = models.IntegerField(null=True, blank=True, editable=False)
    q_issues_qty = models.IntegerField(null=True, blank=True)
    rejected_qty = models.IntegerField(null=True, blank=True)
    total_qty = models.IntegerField(null=True, blank=True)
    first_pass_qty = models.IntegerField(null=True, blank=True)

    #Tiempos
    
    job_process_time = models.FloatField(blank=True, null=True)
    planned_downtime = models.FloatField(blank=True, null=True)
    not_planned_downtime = models.FloatField(blank=True, null=True)

    #Comentarios
    
    job_performance_comments = models.TextField(blank=True, null=True)
    job_quality_comments = models.TextField(blank=True, null=True)

    # Hora inicio / Hora fín
    start_datetime = models.DateTimeField(null=True, blank=True)
    close_datetime = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def job_number(self):
        return self.job_number_id.job_number

    @property
    def item_code(self):
        return self.job_number_id.item_code
    
    @property
    def item_name(self):
        return self.job_number_id.item_name

    @property
    def batch_number(self):
        return self.job_number_id.batch_number
    
    @property
    def get_reworked_qty(self):
        return "Escrbir aqui la fucnion"


    def __str__(self):
        return "Job Partial No %s %s %s Lote:%s" % (self.job_number, self.item_code, self.item_name, self.batch_number)

    