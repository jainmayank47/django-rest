from django.db import models
import email
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UserInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=10,blank=True,null=True)
    email_id = models.EmailField(unique=True)
    mobile_no = models.IntegerField(max_length=12)
    nick_name = models.SlugField(max_length=15,null=True,blank=True)
    role_choice = (("student",1),("teacher",2),("principal",3))
    role = models.CharField(max_length=15,choices=role_choice,default=1)
    status_choice = (("pending",1),("active",2),("inactive",3),("deleted",4))
    gender_choice = (("male","m"),
                    ("female","f"))
    gender = models.CharField(max_length=30,choices=gender_choice,default="m")
    status = models.CharField(max_length=15,choices=status_choice,default=1)
    

    class Meta:
        db_table = "user_info"
        ordering = ["first_name"]