from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from .models import Service_Company, Appointmenttime, Appointment,Subservice




@admin.register(Service_Company)
class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Appointmenttime)
class AppointmentTimeAdmin(admin.ModelAdmin):
    list_display = ('service_company', 'date', 'start_time', 'end_time', 'available')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service_company', 'appointment_time')




class SubserviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Define the fields to display in the admin list view

admin.site.register(Subservice, SubserviceAdmin)

