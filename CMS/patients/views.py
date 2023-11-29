import csv
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from patients.forms import patientForm, treatmentForm
from patients.models import patients, treatment
from staff.models import staffs
from django.contrib import messages


# dashboard
def dashboard(request):
    staff_count = staffs.objects.count()
    patient_count = patients.objects.count()
    context = {
        'staff_count': staff_count,
        'patient_count': patient_count,
        'user': request.user
    }

    return render(request, 'body.html', context)


# patients operations
def viewpatients(request):
    patient = patients.objects.all()
    staff_count = staffs.objects.count()
    patient_count = patients.objects.count()
    treat = treatment.objects.all()
    latest_treats = treatment.objects.order_by('date_treated')[:]
    latest_patients = patients.objects.order_by('date_added')[:]
    context = {
        'patient': patient,
        'treat': treat,
        'staff_count': staff_count,
        'patient_count': patient_count,
        'latest_patients': latest_patients,
        'latest_treats': latest_treats,

    }
    return render(request, 'view_patients.html', context)


def detailed_patient(request, id):
    view = get_object_or_404(patients, id=id)
    context = {
        'patient': view,
    }
    return render(request, 'patient_detailed.html', context)


def addpatient(request):
    if request.method == 'POST':
        form = patientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            patient_name = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            doc_name= form.cleaned_data['staffs'].full_name
            messages.success(request, f'Patient {patient_name} has an appointment to staff {doc_name} ')
            return redirect('patients:view_patients')
    else:
        form = patientForm()
        return render(request, 'add_patients.html', {'form': form})


def patient_update(request, id):
    patient = get_object_or_404(patients, id=id)
    if request.method == 'POST':
        date_added = request.POST.get('date_added')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        patient.date_added = date_added
        patient.first_name = first_name
        patient.last_name = last_name
        patient.date_of_birth = date_of_birth
        patient.gender = gender
        patient.email = email
        patient.phone_number = phone_number
        patient.address = address
        patient.save()

        return redirect('patients:view_patients')

    return render(request, 'update_patient.html', {'patient': patient})



def patient_delete(request, id):
    patient = patients.objects.get(id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients:view_patients')
    return render(request, 'delete_patient.html', {'patient': patient})


def download_table(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patient_table.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Date of Birth', 'Gender', 'Email', 'Phone Number', 'Address'])

    patient = patients.objects.all()
    for patient in patient:
        writer.writerow([patient.first_name, patient.last_name, patient.date_of_birth, patient.gender,
                         patient.email, patient.phone_number, patient.address])

    return response


# treatment operations

def addtreat(request):
    if request.method == 'POST':
        form = treatmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patients:view_patients')
    else:
        form = treatmentForm()
        return render(request, 'add_treat.html', {'form': form})


def treat_update(request, id):
    treat = get_object_or_404(treatment, id=id)
    if request.method == 'POST':
        form = treatmentForm(request.POST, instance=treat)
        if form.is_valid():
            form.save()
            return redirect('patients:view_patients')
    else:
        form = treatmentForm(instance=treat)
        return render(request, 'update_treat.html', {'treat': treat, 'form': form})


def treat_delete(request, id):
    treat = treatment.objects.get(id=id)
    if request.method == 'POST':
        treat.delete()
        return redirect('patients:view_patients')
    return render(request, 'delete_treat.html', {'treat': treat})


def detailed_treat(request, id):
    view = get_object_or_404(treatment, id=id)
    context = {
        'treat': view,
    }
    return render(request, 'detailed_treat.html', context)
