from django.db import models

# Create your models here.


from django.db import models

class Appointmenttime(models.Model):
    Service_Company = models.ForeignKey('Service_Company', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)

class Service_Company(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)




from django.db import models

class Service_Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Appointmenttime(models.Model):
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)


class Appointment(models.Model):
    service_company = models.ForeignKey(Service_Company, on_delete=models.CASCADE)
    appointment_time = models.ForeignKey(Appointmenttime, on_delete=models.CASCADE)


class Subservice(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)    
    # Add any other fields related to the appointment here, such as patient name, etc.




    # Other doctor-related fields


 