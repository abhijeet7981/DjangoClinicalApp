from django.shortcuts import render,redirect
from .models import Patient,ClinicalData
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ClinicalDataForm,PatientForm
import json


# Create your views here.


class PateintListView(ListView):
    model=Patient


class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')



class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')


class PatientdeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')

def addData(request,**kwagrs):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=kwagrs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')



    return render(request,'clinicaldata_form.html',{'form':form,'patient':patient})





def analyze(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    response_data=[]
    for eachEntry in data:
        if eachEntry.componentName=='HW':
            heightWeight=eachEntry.componentValue.split('/')
            if len(heightWeight) >1:
                ht_meter=float(heightWeight[0]) * 0.453
                BMI=(float(heightWeight[1])) / ((ht_meter)**2)
                bmiEntry=ClinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=BMI
                response_data.append(bmiEntry)
        response_data.append(eachEntry)
    return render (request,'genrateReport.html',{'data':response_data})

    print(response_data)


    

