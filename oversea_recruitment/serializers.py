from rest_framework import serializers
from .models import Service_Company,Appointmenttime,Appointment,Subservice,Service_Company,identyverification,categorylist

class ServicecompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Company
        fields = '__all__'







class ServicecompanySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Service_Company
        fields = ('user_name', 'gender', 'date_of_birth','fullname')         

class AppointmenttimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointmenttime
        fields = '__all__'



class GenerateAppointmentSlotsSerializer(serializers.Serializer):
    companyid = serializers.IntegerField()
    date = serializers.DateField()
    num_appointments = serializers.IntegerField()
    interval_minutes = serializers.IntegerField()
    start_time = serializers.CharField()       



class AppointmentSerializer(serializers.ModelSerializer):
    # Add this field for the appointment_time ID

    class Meta:
        model = Appointment
        fields = '__all__'


class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        fields = '__all__'       



class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Company
        fields = '__all__'        



class ServicecompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Company
        fields = '__all__'



        


class identySerializer(serializers.ModelSerializer):
    class Meta:
        model = identyverification
        fields = '__all__'




class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categorylist
        fields = '__all__'