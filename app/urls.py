from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),

    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),

    path('reviews/', views.review_list, name='review_list'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('messages/', views.message_list, name='message_list'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('payments/', views.payment_list, name='payment_list'),
]