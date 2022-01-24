from django.db import models
from datetime import datetime

status_value = (("active","active"),("pending","pending"),("inactive","inactive"))


# Create your models here.    

class TeacherModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    salary = models.IntegerField()
    status = models.CharField(choices=status_value,default="active",max_length=20)
    created_at = models.DateTimeField(default=datetime.now)
    modified_at = models.DateTimeField(default=datetime.now)

    def __str__(self): 
        return self.id+" : "+self.name

