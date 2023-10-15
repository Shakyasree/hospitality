# portal/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm


@login_required
def receptionist_portal(request):
    patients = Patient.objects.filter(receptionist=request.user.receptionist)
    return render(request, 'portal/receptionist_portal.html', {'patients': patients})

@login_required
def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.receptionist = request.user.receptionist
            patient.save()
            return redirect('receptionist_portal')
    else:
        form = PatientForm()
    return render(request, 'portal/register_patient.html', {'form': form})

@login_required
def doctor_portal(request):
    patients = Patient.objects.filter(doctor=request.user.doctor)
    return render(request, 'portal/doctor_portal.html', {'patients': patients})
