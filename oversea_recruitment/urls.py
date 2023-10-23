from django.urls import path
from .views import GenerateAppointmentSlotsView,CreateAppointmentView,SubserviceCreateView,SubserviceListView,ServiceCompanyListView,AppointmenttimeListView,SubserviceListViewuser,serviceCreateView,serviceListView,serviceListViewuser,appointmentListViewuser,AppointmentListViewCompany,subservicelistcategory,AppointmentcreatetimeViewSet,identityCreateView,identyViewuser,categorylistcreate,categorylistall

urlpatterns = [
    # Other URL patterns
    path('generate-appointmentsautomate/', GenerateAppointmentSlotsView.as_view(), name='generate-appointments'),
    path('createapointmenttime/', AppointmentcreatetimeViewSet.as_view({'get': 'list', 'post': 'create'}), name='generate-appointments'),
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



    path('identitycompanycreate/', identityCreateView.as_view(), name='subservice-create'),
   # path('servicescompanylistall/', serviceListView.as_view(), name='subservice-list'),
    path('identitycompanylistuser/', identyViewuser.as_view(), name='subservice-list'),


     path('service-companiesfilter/', ServiceCompanyListView.as_view(), name='service-company-list'),
     path('appointmenttimeslist/', AppointmenttimeListView.as_view(), name='appointmenttime-list'),



     path('categorylistcreate/', categorylistcreate.as_view(), name='product-list-create'),
     path('categorylistall/', categorylistall.as_view(), name='product-detail'),
]
