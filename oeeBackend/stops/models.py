from django.db import models

# Create your models here.

class Stop(models.Model):
    STOP_TYPE_CHOICES = (
        ('NPSTOP', 'Parada no planificada'),
        ('PSTOP', 'Parada planificada')
    )

    stop_name = models.CharField(max_length=256)
    stop_type = models.CharField(
        max_length=6,
        choices=STOP_TYPE_CHOICES
    )
    stop_res_email = models.EmailField(
        max_length=254,
        blank=True, 
        null=True
    )      
    stop_created_at = models.DateTimeField(auto_now_add=True)
    stop_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.stop_type == 'NPSTOP':
            return 'Parada no planificada: {}'.format(self.stop_name)
        else:
            return 'Parada planificada: {}'.format(self.stop_name)

