from django.db import models

# Create your models here.

class QualityIssue(models.Model):

    q_issue = models.CharField(max_length=256)
    rework_rate = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.q_issue