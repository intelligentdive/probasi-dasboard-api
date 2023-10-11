from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Service_Company,Appointmenttime
from .serializers import ServicecompanySerializer,AppointmenttimeSerializer
from datetime import timedelta
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from .models import Service_Company, Appointmenttime,Appointment  # Import your models
from .serializers import GenerateAppointmentSlotsSerializer,AppointmentSerializer


class GenerateAppointmentSlotsView(generics.CreateAPIView):
    serializer_class = GenerateAppointmentSlotsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        company_id = validated_data.get('company')
        date = validated_data.get('date')
        num_appointments = validated_data.get('num_appointments')
        interval_minutes = validated_data.get('interval_minutes')

        # Fetch the company
        company = Service_Company.objects.get(id=company_id)

        # Input start time (you need to provide the input for the start time)
        start_time_input = validated_data.get('start_time')

        if start_time_input is None:
            return Response(
                {'error': 'start_time is required in the request data'},
                status=status.HTTP_400_BAD_REQUEST
            )

        start_time = datetime.strptime(start_time_input, '%H:%M')  # Convert a string input to a datetime

        # Calculate the end time based on the interval duration
        end_time = start_time + timedelta(minutes=num_appointments * interval_minutes)

        delta = timedelta(minutes=interval_minutes)

        appointment_slots = []
        current_time = start_time

        while current_time < end_time:
            end_slot_time = current_time + delta
            if end_slot_time <= end_time:
                # Create and save the appointment directly without a serializer
                appointment = Appointmenttime(
                    service_company=company,
                    date=date,
                    start_time=current_time,
                    end_time=end_slot_time
                )
                appointment.save()
                appointment_slots.append(appointment)
                current_time = end_slot_time
            else:
                break

        return Response(
            {'message': f'{len(appointment_slots)} slots generated successfully'},
            status=status.HTTP_201_CREATED
        )




class CreateAppointmentView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        service_company_id = request.data.get('service_company')
        appointment_time_id = request.data.get('appointment_time')
       

        service_company_id = Service_Company.objects.get(id=service_company_id)

        appointment_time_id = Appointmenttime.objects.get(id=appointment_time_id)
        appointment_time_id.available =False 
        appointment_time_id.save()
        # You may want to validate the existence of the service_company and appointment_time
        try:
            appointment = Appointment.objects.create(
                service_company=service_company_id,
                appointment_time=appointment_time_id
                # Add other fields as needed
            )

          
            return Response({'message': 'Appointment created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




