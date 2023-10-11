from django.urls import path
from .views import GenerateAppointmentSlotsView,CreateAppointmentView

urlpatterns = [
    # Other URL patterns
    path('generate-appointments/', GenerateAppointmentSlotsView.as_view(), name='generate-appointments'),
    path('create-appointment/', CreateAppointmentView.as_view(), name='create-appointment'),
]
