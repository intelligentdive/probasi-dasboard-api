from django.db import models

# Create your models here.

from django.db import models
from django.db import models

from user.models import User

class Service_Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)






class Subservice(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)  
    country = models.CharField(max_length=100,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    region = models.CharField(max_length=100,blank=True,null=True)
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name


    
    
    



class Appointmenttime(models.Model):
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)


class Appointment(models.Model):
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)
    appointment_time = models.ForeignKey(Appointmenttime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    phone= models.CharField(max_length=100,blank=True,null=True) 
    email = models.EmailField(
       
        max_length=255,
        
        blank=True,
        null=True,
    )
    note= models.CharField(max_length=1000,blank=True,null=True) 

  
    # Add any other fields related to the appointment here, such as patient name, etc.



# class Appointmenttime(models.Model):
#     Service_Company = models.ForeignKey('Service_Company', on_delete=models.CASCADE)
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     available = models.BooleanField(default=True)
#     # Other doctor-related fields


 