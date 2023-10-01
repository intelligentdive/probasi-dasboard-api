from django.urls import path
from .views import DistrictList, CompanyListCreateView, CompanyDetailView, ExpertiseListCreateView
from . import views

urlpatterns = [
    path('districts/', DistrictList.as_view(), name='district-list'),
    path('countries/', views.CountryListCreateView.as_view(), name='country-list'),
    path('countries/<int:pk>/', views.CountryDetailView.as_view(), name='country-detail'),
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('expertise/', ExpertiseListCreateView.as_view(), name='expertise-list-create'),
]