from django.db import models

# Create your models here.


class Patient(models.Model):
    firstName=models.CharField(max_length=19)
    lastName=models.CharField(max_length=19)
    age=models.IntegerField()


class ClinicalData(models.Model):
    COMPONENT_NAME=[('HW','Height/Weight'),('BP','Blood Pressure'),('HR','Heart Rate')]
    componentName=models.CharField(choices=COMPONENT_NAME, max_length=50)
    componentValue=models.CharField(max_length=50)
    measuredDateTime=models.DateTimeField(auto_now_add=True)
    patient= models.ForeignKey(Patient,on_delete=models.CASCADE)

