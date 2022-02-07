from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
        

class TechnologyInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    status_choices= (("active","active"),("inactive","inactive"),("pending","pending"))
    status = models.CharField(max_length=15,choices=status_choices,default="pending")
    class Meta:
        db_table = "technology_info"
        ordering = ["name"]
        
class FrameworkInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    technology = models.ForeignKey(TechnologyInfo,db_column="technology",related_name = 'framework',on_delete=models.CASCADE)
    class Meta:
        db_table = "framework_info"

