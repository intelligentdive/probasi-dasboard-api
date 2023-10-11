from rest_framework import serializers
from .models import Service_Company,Appointmenttime,Appointment

class ServicecompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Company
        fields = '__all__'

class AppointmenttimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointmenttime
        fields = '__all__'



class GenerateAppointmentSlotsSerializer(serializers.Serializer):
    company = serializers.IntegerField()
    date = serializers.DateField()
    num_appointments = serializers.IntegerField()
    interval_minutes = serializers.IntegerField()
    start_time = serializers.CharField()       



class AppointmentSerializer(serializers.ModelSerializer):
    # Add this field for the appointment_time ID

    class Meta:
        model = Appointment
        fields = '__all__'
