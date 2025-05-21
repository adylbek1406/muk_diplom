from django.shortcuts import render
from .models import Doctor, Patient, Appointment, Review, ConsultationRequest, Message, Prescription, Payment


def home_view(request):
    return render(request, 'home.html')


def doctor_list(request):
    return render(request, 'doctors/doctor_list.html', {'doctors': Doctor.objects.all()})


def doctor_detail(request, pk):
    return render(request, 'doctors/doctor_detail.html', {'doctor': Doctor.objects.get(pk=pk)})


def patient_list(request):
    return render(request, 'patients/patient_list.html', {'patients': Patient.objects.all()})


def patient_detail(request, pk):
    return render(request, 'patients/patient_detail.html', {'patient': Patient.objects.get(pk=pk)})


def appointment_list(request):
    return render(request, 'appointments/appointment_list.html', {'appointments': Appointment.objects.all()})


def appointment_detail(request, pk):
    return render(request, 'appointments/appointment_detail.html', {'appointment': Appointment.objects.get(pk=pk)})


def review_list(request):
    return render(request, 'reviews/review_list.html', {'reviews': Review.objects.all()})


def consultation_list(request):
    return render(request, 'consultations/consultation_list.html', {'consultations': ConsultationRequest.objects.all()})


def message_list(request):
    return render(request, 'messages/message_list.html', {'messages': Message.objects.all()})


def prescription_list(request):
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': Prescription.objects.all()})


def payment_list(request):
    return render(request, 'payments/payment_list.html', {'payments': Payment.objects.all()})
