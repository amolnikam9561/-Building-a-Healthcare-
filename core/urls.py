from django.urls import path
from .views import RegisterView
from .views import (
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingByPatientView, MappingDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
    # Patient endpoints
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Doctor endpoints
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Mapping endpoints
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/patient/<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
