from django.urls import path
from .views import GenerateAppointmentSlotsView,CreateAppointmentView,SubserviceCreateView,SubserviceListView,ServiceCompanyListView,AppointmenttimeListView,SubserviceListViewuser,serviceCreateView,serviceListView,serviceListViewuser,appointmentListViewuser,AppointmentListViewCompany,subservicelistcategory

urlpatterns = [
    # Other URL patterns
    path('generate-appointments/', GenerateAppointmentSlotsView.as_view(), name='generate-appointments'),
    path('create-appointment/', CreateAppointmentView.as_view(), name='create-appointment'),
    path('appointmentlistuser/', appointmentListViewuser.as_view(), name='create-appointment'),
    path('appointmentlistcompany/', AppointmentListViewCompany.as_view(), name='create-appointment'),


    path('subservicescreate/', SubserviceCreateView.as_view(), name='subservice-create'),
    path('subserviceslistall/', SubserviceListView.as_view(), name='subservice-list'),
    path('subserviceslistuser/', SubserviceListViewuser.as_view(), name='subservice-list'),
    path('subserviceslistcategory/', subservicelistcategory.as_view(), name='subservice-list'),


    path('servicescompanycreate/', serviceCreateView.as_view(), name='subservice-create'),
    path('servicescompanylistall/', serviceListView.as_view(), name='subservice-list'),
    path('servicescompanylistuser/', serviceListViewuser.as_view(), name='subservice-list'),


     path('service-companiesfilter/', ServiceCompanyListView.as_view(), name='service-company-list'),
     path('appointmenttimeslist/', AppointmenttimeListView.as_view(), name='appointmenttime-list'),
]
