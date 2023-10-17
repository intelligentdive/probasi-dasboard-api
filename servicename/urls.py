from django.urls import path
from .views import ServiceCreateView, ServiceListView

urlpatterns = [
    path('servicecreate/', ServiceCreateView.as_view(), name='service-list-create'),
    path('service_list/', ServiceListView.as_view(), name='service-detail-update-delete'),
   
]
