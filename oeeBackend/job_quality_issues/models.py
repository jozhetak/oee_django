from django.db import models
from quality_issues.models import QualityIssue
from job_orders_data.models import JobOrderData

# Create your models here.

class JobQualityIssue(models.Model):
    
    job_order_data_id = models.ForeignKey(
        JobOrderData,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
        related_name='%(class)s_q_issue'
    )
    q_issue_id = models.ForeignKey(
        QualityIssue,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
        related_name='%(class)s_q_issue'
    )
    q_issue_qty = models.IntegerField(blank=False, null=False)
    reworked = models.NullBooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def q_issue(self):
        return self.q_issue_id.q_issue
    
    def __str__(self):
        return self.q_issue