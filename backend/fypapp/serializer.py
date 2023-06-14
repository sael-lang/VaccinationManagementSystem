from rest_framework import serializers
from . models import *


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = [ 'adminEmail','adminPassword']


class access(serializers.ModelSerializer):
    class Meta:
        model = accesslevel
        fields = ['email', 'password','access',]


class DirectorEPISerializer(serializers.ModelSerializer):
    adminEmail = serializers.SlugRelatedField(slug_field='adminEmail', queryset=admin.objects.all())

    class Meta:
        model = directorEPI
        fields = '__all__'

class VaccineManagerSerializer(serializers.ModelSerializer):
    adminEmail = serializers.SlugRelatedField(slug_field='adminEmail', queryset=admin.objects.all())

    class Meta:
        model = VaccineManager
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    adminEmail = serializers.SlugRelatedField(slug_field='adminEmail', queryset=admin.objects.all())

    class Meta:
        model = hospital
        fields = '__all__'


class medicalSuperIntendentSerializer(serializers.ModelSerializer):
    adminEmail = serializers.SlugRelatedField(slug_field='adminEmail', queryset=admin.objects.all())
    hospitalID = serializers.SlugRelatedField(slug_field='id', queryset=hospital.objects.all())

    class Meta:
        model = medicalSuperIntendent
        fields = '__all__'


class vaccineSerializer(serializers.ModelSerializer):
    VM_Email = serializers.SlugRelatedField(slug_field='VM_Email', queryset=VaccineManager.objects.all())

    class Meta:
        model = vaccine
        fields = '__all__'

class VaccineAssignedToDirectorEPISerializer(serializers.ModelSerializer):
    directorEPI_ID = serializers.PrimaryKeyRelatedField(queryset=directorEPI.objects.all())
    VM_Email = serializers.SlugRelatedField(slug_field='VM_Email', queryset=VaccineManager.objects.all())
    assigned_vaccine_id = serializers.PrimaryKeyRelatedField(queryset=vaccine.objects.all())
    vaccineName = serializers.CharField(source='assigned_vaccine_id.vaccineName', required=False)
    directorEPIfullName = serializers.CharField(source='directorEPI_ID.directorEPIfullName', required=False)

    class Meta:
        model = VaccineAssignedToDirectorEPI
        fields = ['id', 'directorEPI_ID', 'assigned_vaccine_id', 'vaccineName', 'Vaccine_Quantity', 'VM_Email', 'directorEPIfullName']


class VaccineAssignedToHospitalSerializer(serializers.ModelSerializer):
    Hospital_ID = serializers.PrimaryKeyRelatedField(queryset=hospital.objects.all())
    DirectorEPI_Email = serializers.SlugRelatedField(slug_field='directorEPIEmail', queryset=directorEPI.objects.all())
    assigned_vaccine_id = serializers.PrimaryKeyRelatedField(queryset=vaccine.objects.all())
    vaccineName = serializers.CharField(source='assigned_vaccine_id.vaccineName', required=False)
    hospitalName = serializers.CharField(source='Hospital_ID.hospitalName', required=False)

    class Meta:
        model = VaccineAssignedToHospital
        fields = ['id', 'Hospital_ID', 'assigned_vaccine_id', 'Vaccine_Quantity', 'DirectorEPI_Email','vaccineName','hospitalName']

class HealthCareWorkerAdminSerializer(serializers.ModelSerializer):
    directorEPI_Email = serializers.SlugRelatedField(slug_field='directorEPIEmail', queryset=directorEPI.objects.all())

    class Meta:
        model = HealthCareWorkerAdmin
        fields = '__all__'

class VaccineAssignedToHealthCareWorkerAdminSerializer(serializers.ModelSerializer):
    directorEPI_Email = serializers.SlugRelatedField(slug_field='directorEPIEmail', queryset=directorEPI.objects.all())
    hcwAdminID = serializers.SlugRelatedField(slug_field='id', queryset=HealthCareWorkerAdmin.objects.all())
    assigned_vaccine_id = serializers.PrimaryKeyRelatedField(queryset=vaccine.objects.all())
    vaccineName = serializers.CharField(source='assigned_vaccine_id.vaccineName', required=False)
    HCWA_fullName = serializers.CharField(source='hcwAdminID.fullName', required=False)

    class Meta:
        model = VaccineAssignedToHealthCareWorkerAdmin
        fields = ['id', 'hcwAdminID', 'assigned_vaccine_id', 'vaccineName', 'Vaccine_Quantity', 'directorEPI_Email','HCWA_fullName']


class healthcareworkerSerializer(serializers.ModelSerializer):
    HCWA_Email = serializers.SlugRelatedField(slug_field='email', queryset=HealthCareWorkerAdmin.objects.all())

    class Meta:
        model = healthcareworker
        fields = '__all__'

class vaccineAssignedToHCWSerializer(serializers.ModelSerializer):
    HCWA_Email = serializers.SlugRelatedField(slug_field='email', queryset=HealthCareWorkerAdmin.objects.all())
    assigned_vaccine_id = serializers.PrimaryKeyRelatedField(queryset=vaccine.objects.all())
    HCW_ID = serializers.SlugRelatedField(slug_field='id', queryset=healthcareworker.objects.all())
    vaccineName = serializers.CharField(source='assigned_vaccine_id.vaccineName', required=False)
    
    class Meta:
        model = vaccineAssignedToHCW
        fields = ['id', 'assigned_vaccine_id', 'HCW_ID', 'Vaccine_Quantity', 'HCWA_Email', 'vaccineName']

class OperatingStaffSerializer(serializers.ModelSerializer):
    MSI_Email = serializers.SlugRelatedField(slug_field='medicalSuperIntendentEmail', queryset=medicalSuperIntendent.objects.all())
    Hospital_ID = serializers.SlugRelatedField(slug_field='id', queryset=hospital.objects.all())

    class Meta:
        model = OperatingStaff
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class birthRecordSerializer(serializers.ModelSerializer):
    Father_CNIC = serializers.SlugRelatedField(slug_field='id', queryset=Parent.objects.all())
    class Meta:
        model = birthRecord
        fields = '__all__'


class vaccineRecordSerializer(serializers.ModelSerializer):
    childId = serializers.SlugRelatedField(slug_field='id', queryset=birthRecord.objects.all())
    VaccineId = serializers.SlugRelatedField(slug_field='id', queryset=vaccine.objects.all())
    vaccineName = serializers.CharField(source='VaccineId.vaccineName', required=False)
    childName = serializers.CharField(source='childId.fullName', required=False)
    
    class Meta:
        model = vaccineRecord
        fields = ['id', 'childId', 'VaccineId', 'Description', 'RegisteredBy', 'vaccineName', 'childName', 'vaccination_Time']


class FeedbackSerializer(serializers.ModelSerializer):
    Father_Email = serializers.SlugRelatedField(slug_field='Father_Email', queryset=Parent.objects.all())

    class Meta:
        model = feedback
        fields = '__all__'


class future_vaccinesSerializer(serializers.ModelSerializer):
    child_id = serializers.SlugRelatedField(slug_field='id', queryset=birthRecord.objects.all())
    VaccineId = serializers.SlugRelatedField(slug_field='id', queryset=vaccine.objects.all())
    vaccineName = serializers.CharField(source='VaccineId.vaccineName', required=False)
    childName = serializers.CharField(source='child_id.fullName', required=False)
    parent_address = serializers.CharField(source='child_id.Father_CNIC.Address', required=False)
    parent_contact = serializers.CharField(source='child_id.Father_CNIC.Contact', required=False)
    
    class Meta:
        model = future_vaccines
        fields = '__all__'