from django.db import models
from datetime import datetime

status_choices = (('pending', 'pending'),
        ('active', 'active'), 
        ('in-active','in-active'),
        )
# Create your models here.
class studentModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=15,choices=status_choices,default='pending')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
            return self.id +" : "+self.name