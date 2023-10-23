from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Service_Company,Appointmenttime,identyverification
from .serializers import ServicecompanySerializer,AppointmenttimeSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Service_Company, Appointmenttime,Appointment,Subservice,categorylist  # Import your models
from .serializers import GenerateAppointmentSlotsSerializer,AppointmentSerializer,ServiceCompanySerializer,identySerializer,categorySerializer,identySerializer1
from .serializers import SubserviceSerializer
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Q


from rest_framework import views, response, exceptions, permissions

from datetime import datetime,timedelta


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
#from .serializer import UserCreateSerializerphone,UserCreateSerializeremail,ProfileCreateSerializer,Profileloactionbd,Profileloactionabroad,Profileinfoexperienceserializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#from .models import Profileinfo1,Profileinfolocationbd,Profileinfolocationabroad,Profileinfoexperience
import jwt
from rest_framework.exceptions import AuthenticationFailed
from user.models import User

from django.conf import settings
from django.core.mail import send_mail
import random

class GenerateAppointmentSlotsView(generics.CreateAPIView):
    serializer_class = GenerateAppointmentSlotsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        company_id = validated_data.get('companyid')
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

        try:
            start_time = datetime.strptime(start_time_input, '%H:%M')
        except ValueError:
            return Response(
                {'error': 'Invalid start_time format. It should be in the format HH:MM'},
                status=status.HTTP_400_BAD_REQUEST
            )

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

    # def create(self, request, *args, **kwargs):
    #     service_company_id = request.data.get('service_company')
    #     appointment_time_id = request.data.get('appointment_time')
       

    #     service_company_id = Service_Company.objects.get(id=service_company_id)

    #     appointment_time_id = Appointmenttime.objects.get(id=appointment_time_id)
    #     appointment_time_id.available =False 
    #     appointment_time_id.save()
        # You may want to validate the existence of the service_company and appointment_time
    def post(self, request):
        # Ensure that the user does not already have a profile
        service_company_id = request.data.get('service_company')
        appointment_time_id = request.data.get('appointment_time')
       

        service_company_id = Service_Company.objects.get(id=service_company_id)

        appointment_time_id = Appointmenttime.objects.get(id=appointment_time_id)
        appointment_time_id.available =False 
        appointment_time_id.save()



        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')





       

        serializer =AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







#sub service start

class SubserviceCreateView(views.APIView):
    

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')





       

        serializer =SubserviceSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class SubserviceListView(generics.ListAPIView):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer



class SubserviceListViewuser(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id'])

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Subservice.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = SubserviceSerializer(profile,many= True)

        return Response(serializer.data)   
    


class subservicelistcategory(views.APIView):

    def post(self, request):
        # Retrieve the JSON data from the request body
        data = request.data
        category1 = data.get('category', None)

        if category1 is None:
            return Response({'error': 'Category not provided in request data'}, status=status.HTTP_400_BAD_REQUEST)
            
        appointments = Subservice.objects.filter(category=category1)
        serializer = SubserviceSerializer(appointments, many=True)
        return Response(serializer.data)
           



#subservice end

#service start comapany

class serviceCreateView(views.APIView):
    

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')





       

        serializer =ServiceCompanySerializer(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class serviceListView(generics.ListAPIView):
    queryset = Service_Company.objects.all()
    serializer_class = ServiceCompanySerializer



class serviceListViewuser(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  Service_Company.objects.filter(user=user).first()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = ServiceCompanySerializer(profile)

        return Response(serializer.data)   

#service end





#identity start comapany

class identityCreateView(views.APIView):
    

    def post(self, request):
        # Ensure that the user does not already have a profile

        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1]

        if not token:
            raise AuthenticationFailed('Invalid or missing token!')

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user1 = User.objects.filter(id=payload['id']).first()

        if not user1:
            raise AuthenticationFailed('User not found!')





       

        serializer =identySerializer1(data=request.data)
        if serializer.is_valid():
            # Create a new profile for the authenticated user
            serializer.save(user=user1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 






class identyViewuser(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile =  identyverification.objects.filter(user=user).all()

        if not profile:
            raise AuthenticationFailed('Profile not found!')

        # You should import and use your profile serializer here
        serializer = identySerializer(profile,many=True)

        return Response(serializer.data)   
    







#identity end










#filter
class ServiceCompanyListView(generics.ListCreateAPIView):
    queryset = Subservice.objects.all()
    serializer_class = ServiceCompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'region', 'subserviceid', 'name']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Perform the filtering based on GET request parameters here

        return queryset

    def create(self, request, *args, **kwargs):
        country = request.data.get('country', None)
        region = request.data.get('region', None)
        subservice_id = request.data.get('subserviceid', None)
        name1 = request.data.get('companyname', None)

        # Create an empty Q object to combine the filter conditions
        combined_filter = Q()

        if country:
            combined_filter &= Q(country=country)

        if region:
            combined_filter &= Q(region=region)

        if subservice_id:
            combined_filter &= Q(id=subservice_id)

        # Apply the combined filter to the queryset
        queryset = Subservice.objects.filter(combined_filter)

        # Fetch ServiceCompany instances related to the filtered Subservice objects
        service_companies = Service_Company.objects.filter(subservice__in=queryset).distinct()

        # Add a filter by the 'name' field if provided in the request body
        if name1:
            service_companies = service_companies.filter(name=name1)

        serializer = self.get_serializer(service_companies, many=True)
        return Response(serializer.data)







    





class AppointmenttimeListView(generics.ListAPIView):
    serializer_class = AppointmenttimeSerializer

    def get_queryset(self):
        data = self.request.data
        service_company_id = data.get('service_company_id', None)
        date = data.get('date', None)

        queryset = Appointmenttime.objects.filter(available=True)

        if service_company_id and date:
            queryset = queryset.filter(
                Q(service_company__id=service_company_id) &
                Q(date=date)
            )
        elif service_company_id:
            queryset = queryset.filter(service_company__id=service_company_id)
        elif date:
            queryset = queryset.filter(date=date)

        return queryset

    def post(self, request, *args, **kwargs):
        # Perform filtering based on the JSON data in the request body
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class appointmentListViewuser(views.APIView):

    def get(self, request):
        # Retrieve the JWT token from the Authorization header
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid or missing Bearer token!')

        token = authorization_header.split('Bearer ')[1].strip()  # Strip whitespaces

        try:
            # Make sure to use the same secret key that was used to encode the JWT
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT has expired!')
        except jwt.DecodeError:
            raise AuthenticationFailed('JWT is invalid!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        profile = Appointment.objects.filter(user=user)

        

        # You should import and use your profile serializer here
        serializer = AppointmentSerializer(profile,many=True)

        return Response(serializer.data)  





class AppointmentListViewCompany(views.APIView):

    def get(self, request):
        # Retrieve the companyid from the request parameters or query parameters
        data = self.request.data
        company_id = data.get('companyid', None)

        if company_id is not None:
            # Assuming you have a Service_Company model with an 'id' field
            try:
                company = Service_Company.objects.get(id=company_id)
                appointments = Appointment.objects.filter(company=company)
                serializer = AppointmentSerializer(appointments, many=True)
                return Response(serializer.data)
            except Service_Company.DoesNotExist:
                return Response({"error": "Company not found"}, status=404)
        else:
            return Response({"error": "Missing 'companyid' parameter"}, status=400)
        



       



class AppointmentcreatetimeViewSet(viewsets.ModelViewSet):
    queryset = Appointmenttime.objects.all()
    serializer_class = AppointmenttimeSerializer  

    # Create a new instance of YourModel

    





class categorylistcreate(generics.ListCreateAPIView):
    queryset = categorylist.objects.all()
    serializer_class = categorySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class categorylistall(generics.ListAPIView):
    queryset = categorylist.objects.all()
    serializer_class = categorySerializer






class identitylistcompany(views.APIView):

    def post(self, request):
        # Retrieve the JSON data from the request body
        data = request.data
        comid = data.get('companyid', None)

        if comid is None:
            return Response({'error': 'Category not provided in request data'}, status=status.HTTP_400_BAD_REQUEST)
            
        appointments =identyverification.objects.filter(service_company__id=comid)
        serializer = identySerializer(appointments, many=True)
        return Response(serializer.data)