# portal/urls.py

from django.urls import path
from .views import receptionist_portal, register_patient, doctor_portal

urlpatterns = [
    path('receptionist-portal/', receptionist_portal, name='receptionist_portal'),
    path('register-patient/', register_patient, name='register_patient'),
    path('doctor-portal/', doctor_portal, name='doctor_portal'),
]
