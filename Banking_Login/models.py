from django.db import models
from django.contrib.auth.models import User

class Banking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.name
    
class Account_Creation(models.Model):
    # user = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
    First_Name = models.CharField(max_length=100,null=True)
  
    Adhaar_Card_Image = models.ImageField(upload_to='static/Images/Adhaar_Card',null=True)
    Pan_Card_Image = models.ImageField(upload_to="static/Images/Pan_Card_Image",null=True)
    Last_Name = models.CharField(max_length=100,null=True)
    Adhaar_Card_Number = models.CharField(max_length=100,unique = True,null=True)
    Pan_Card_Number = models.CharField(max_length=100 , unique=True,null=True)
    Permanant_Address = models.CharField(max_length=200,null=True)
    Resdential_Address = models.CharField(max_length=200,null=True)
    Personal_Image = models.ImageField(upload_to='static/Images/Personal_Image',null=True)
    Account_Number = models.CharField(max_length=200,null=True,unique = True)
    Basic_Amount = models.IntegerField(null=True)
    Password = models.CharField(max_length=100,null=True)
#https://www.javatpoint.com/django-orm-queries
