from django.db import models

# Create your models here.

class Item(models.Model):

    item_code = models.CharField(max_length=12)
    item_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s: %s'%(self.item_code, self.item_name)