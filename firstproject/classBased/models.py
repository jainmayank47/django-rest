import email
from django.db import models

# Create your models here.

class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class StudentInfoModel(baseModel):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20,null=True,blank=True)
    gender_choice = (("male","m"),
                    ("female","f"))
    gender = models.CharField(max_length=30,choices=gender_choice,default="m")
    status_choice = (("active","active"),
                    ("inactive","inactive"),
                    ("pending","pending"),
                    ("deleted","deleted"))
    status = models.CharField(max_length=10,choices=status_choice,default="pending")
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    nick_name = models.SlugField(max_length=10)
    semester = models.IntegerField()

    class Meta:
        db_table = "student_info" 
        ordering = ["first_name"]



