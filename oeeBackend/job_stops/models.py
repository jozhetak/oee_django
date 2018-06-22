from django.db import models
from job_orders_data.models import JobOrderData
from stops.models import Stop
from datetime import datetime
import time


# Create your models here.

class JobStop(models.Model):

    job_order_data_id = models.ForeignKey(
        JobOrderData,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
        related_name='%(class)s_job_order_data'
    )
    stop_id = models.ForeignKey(
        Stop,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
        related_name='%(class)s_q_issue'
    )

    # Hora inicio / Hora fín

    start_datetime = models.DateTimeField(null=True, blank=True)
    close_datetime = models.DateTimeField(null=True, blank=True)

    #Tiempos
    
    stop_time = models.FloatField(blank=True, null=True, editable=False)

    #Comentarios
    
    stop_description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def stop_name(self):
        return self.stop_id.stop_name

    @property
    def get_stop_time(self):
        return (self.close_datetime - self.start_datetime).total_seconds() / 60
    
    def save(self, *args, **kwargs):
        self.stop_time = self.get_stop_time
        super(JobStop, self).save(*args, **kwargs)


    def __str__(self):
        return self.stop_name

    