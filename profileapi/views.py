from rest_framework import generics
from .models import District, Country, Company, Expertise
from .serializers import DistrictSerializer, CountrySerializer, CompanySerializer, ExpertiseSerializer

class DistrictList(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class ExpertiseListCreateView(generics.ListCreateAPIView):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer

