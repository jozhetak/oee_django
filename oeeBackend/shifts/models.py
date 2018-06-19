from django.db import models

# Create your models here.

class Shift(models.Model):

    SHIFT_NAME_CHOICES = (
        ('A', 'Turno A'),
        ('B', 'Turno B'),
        ('C', 'Turno C'),
    )

    shift_name = models.CharField(
        max_length=8,
        choices=SHIFT_NAME_CHOICES,
    )
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shift_name