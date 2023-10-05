from django.urls import path
from .views import ServiceListCreateView, ServiceDetailUpdateDeleteView

urlpatterns = [
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailUpdateDeleteView.as_view(), name='service-detail-update-delete'),
]
