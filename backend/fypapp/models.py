from django.db import models

# Create your models here.
class admin(models.Model):
    adminEmail=models.CharField(max_length=15, primary_key=True)
    adminPassword=models.CharField(max_length=16)


class accesslevel(models.Model):
    email=models.CharField(max_length=25, primary_key=True)
    password=models.CharField(max_length=25)
    access=models.CharField(max_length=25)

class VaccineManager(models.Model):
    VM_FullName=models.CharField(max_length=80)
    VM_Email=models.CharField(max_length=50, unique=True)
    VM_Password=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    province=models.CharField(max_length=15)
    adminEmail = models.ForeignKey(admin, on_delete=models.CASCADE, to_field='adminEmail')
    id=models.CharField(max_length=15, primary_key=True)

class vaccine(models.Model):
    id=models.AutoField(primary_key=True)
    vaccineName=models.CharField(max_length=50)
    vaccinetype=models.CharField(max_length=50)
    vaccinequantity=models.IntegerField()
    vaccinedescription=models.CharField(max_length=255)
    VM_Email = models.ForeignKey(VaccineManager, on_delete=models.CASCADE, to_field='VM_Email')

class directorEPI(models.Model):
    adminEmail = models.ForeignKey(admin, on_delete=models.CASCADE, to_field='adminEmail')
    directorEPIfullName = models.CharField(max_length=80)
    directorEPIEmail = models.CharField(max_length=50, unique=True)
    directorEPIPassword = models.CharField(max_length=20)
    directorEPIProvince = models.CharField(max_length=25)
    directorEPIphone = models.CharField(max_length=15, unique=True)
    id = models.CharField(max_length=15, primary_key=True)


class hospital(models.Model):
    id = models.AutoField(primary_key=True)
    hospitalName=models.CharField(max_length=100)
    hospitalCity=models.CharField(max_length=100)
    hospitalProvince=models.CharField(max_length=50)
    hospitalAddress=models.CharField(max_length=150)
    adminEmail = models.ForeignKey(admin, on_delete=models.CASCADE, to_field='adminEmail')

class medicalSuperIntendent(models.Model):
    id=models.CharField(max_length=15, primary_key=True)
    medicalSuperIntendentEmail=models.CharField(max_length=15, unique=True)
    medicalSuperIntendentPassword=models.CharField(max_length=15)
    medicalSuperIntendentFullName=models.CharField(max_length=25)
    phone=models.CharField(max_length=15)
    hospitalID = models.OneToOneField(hospital, on_delete=models.CASCADE, to_field='id', unique=True)
    adminEmail = models.ForeignKey(admin, on_delete=models.CASCADE, to_field='adminEmail')

class VaccineAssignedToDirectorEPI(models.Model):
    id = models.AutoField(primary_key=True)
    directorEPI_ID = models.ForeignKey(directorEPI, on_delete=models.CASCADE, to_field='id')
    assigned_vaccine_id = models.ForeignKey(vaccine, on_delete=models.CASCADE, to_field='id', related_name='assigned_vaccine')
    Vaccine_Quantity=models.IntegerField() #Quantity
    VM_Email = models.ForeignKey(VaccineManager, on_delete=models.CASCADE, to_field='VM_Email')

    class Meta:
        unique_together = (("directorEPI_ID", "assigned_vaccine_id"),)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if primary key is assigned
            assigned_vaccine_id = self.assigned_vaccine_id
            assigned_vaccine_id.vaccinequantity -= self.Vaccine_Quantity
            assigned_vaccine_id.save()
        super().save(*args, **kwargs)


class VaccineAssignedToHospital(models.Model):
    id = models.AutoField(primary_key=True)
    Hospital_ID = models.ForeignKey(hospital, on_delete=models.CASCADE, to_field='id')
    assigned_vaccine_id = models.ForeignKey(vaccine, on_delete=models.CASCADE, to_field='id')
    Vaccine_Quantity=models.IntegerField() 
    DirectorEPI_Email = models.ForeignKey(directorEPI, on_delete=models.CASCADE, to_field='directorEPIEmail')

    class Meta:
        unique_together = (("Hospital_ID", "assigned_vaccine_id"),)

    def save(self, *args, **kwargs):
        is_new_record = not bool(self.id)
        super().save(*args, **kwargs)
        if is_new_record:
            assigned_vaccine_id = self.assigned_vaccine_id
            directorEPI_Email = self.DirectorEPI_Email
            vaccine_assigned_to_epi = VaccineAssignedToDirectorEPI.objects.filter(
                directorEPI_ID=directorEPI_Email.id,
                assigned_vaccine_id=assigned_vaccine_id
            ).first()

            if vaccine_assigned_to_epi:
                vaccine_assigned_to_epi.Vaccine_Quantity -= self.Vaccine_Quantity
                vaccine_assigned_to_epi.save()


class HealthCareWorkerAdmin(models.Model):
    fullName=models.CharField(max_length=80)
    email=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=20)
    contact=models.CharField(max_length=15)
    directorEPI_Email = models.ForeignKey(directorEPI, on_delete=models.CASCADE, to_field='directorEPIEmail')
    province=models.CharField(max_length=15)
    region=models.CharField(max_length=50, unique=True)
    id=models.CharField(max_length=20, primary_key=True)

class VaccineAssignedToHealthCareWorkerAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    hcwAdminID = models.ForeignKey(HealthCareWorkerAdmin, on_delete=models.CASCADE, to_field='id')
    assigned_vaccine_id = models.ForeignKey(vaccine, on_delete=models.CASCADE, to_field='id')
    Vaccine_Quantity=models.IntegerField()
    directorEPI_Email = models.ForeignKey(directorEPI, on_delete=models.CASCADE, to_field='directorEPIEmail')

    class Meta:
        unique_together = (("hcwAdminID", "assigned_vaccine_id"),)

    def save(self, *args, **kwargs):
        is_new_record = not self.pk
        super().save(*args, **kwargs)
        
        if is_new_record:
            assigned_vaccine_id = self.assigned_vaccine_id
            directorEPI_Email = self.directorEPI_Email
            vaccine_assigned_to_epi = VaccineAssignedToDirectorEPI.objects.filter(
                directorEPI_ID=directorEPI_Email.id,
                assigned_vaccine_id=assigned_vaccine_id
            ).first()

            if vaccine_assigned_to_epi:
                vaccine_assigned_to_epi.Vaccine_Quantity -= self.Vaccine_Quantity
                vaccine_assigned_to_epi.save()

class healthcareworker(models.Model):
    id=models.CharField(max_length=20, primary_key=True)
    Email=models.CharField(max_length=150, unique=True)
    Password=models.CharField(max_length=15)
    fullName=models.CharField(max_length=150)
    contact=models.CharField(max_length=15)
    region=models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    HCWA_Email = models.ForeignKey(HealthCareWorkerAdmin, on_delete=models.CASCADE, to_field='email')


class vaccineAssignedToHCW(models.Model):
    id = models.AutoField(primary_key=True)
    assigned_vaccine_id = models.ForeignKey(vaccine, on_delete=models.CASCADE, to_field='id')
    HCW_ID = models.ForeignKey(healthcareworker, on_delete=models.CASCADE, to_field='id')
    Vaccine_Quantity=models.IntegerField()
    HCWA_Email = models.ForeignKey(HealthCareWorkerAdmin, on_delete=models.CASCADE, to_field='email')

    class Meta:
        unique_together = (("HCW_ID", "assigned_vaccine_id"),)

    def save(self, *args, **kwargs):
        is_new_record = not self.pk
        super().save(*args, **kwargs)
        
        if is_new_record:
            assigned_vaccine_id = self.assigned_vaccine_id
            HCWA_Email = self.HCWA_Email
            vaccine_assigned_to_epi = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(
                hcwAdminID=HCWA_Email.id,
                assigned_vaccine_id=assigned_vaccine_id
            ).first()

            if vaccine_assigned_to_epi:
                vaccine_assigned_to_epi.Vaccine_Quantity -= self.Vaccine_Quantity
                vaccine_assigned_to_epi.save()

class OperatingStaff(models.Model):
    OS_fullName=models.CharField(max_length=80)
    OS_Email=models.CharField(max_length=50, unique=True)
    OS_Password=models.CharField(max_length=20)
    OS_Contact=models.CharField(max_length=15)
    MSI_Email = models.ForeignKey(medicalSuperIntendent, on_delete=models.CASCADE, to_field='medicalSuperIntendentEmail')
    Hospital_ID = models.ForeignKey(hospital, on_delete=models.CASCADE, to_field='id')
    id=models.CharField(max_length=20, primary_key=True)

class Parent(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    Contact = models.CharField(max_length=15)
    Mother_CNIC = models.CharField(max_length=20)
    Father_Email = models.CharField(max_length=150, unique=True)
    Password = models.CharField(max_length=15)
    City = models.CharField(max_length=80)
    Address = models.CharField(max_length=200)

class birthRecord(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    fullName = models.CharField(max_length=150)
    Gender = models.CharField(max_length=10)
    childWeight = models.FloatField(null=True)
    childLength = models.FloatField(null=True)
    deliveryType = models.CharField(max_length=25, null=True)
    birth_date = models.CharField(max_length=200)
    Hospital_ID = models.IntegerField(null=True)
    RegisteredBy = models.CharField(max_length=150)
    Father_CNIC = models.ForeignKey(Parent, on_delete=models.CASCADE, to_field='id')

class vaccineRecord(models.Model):
    id = models.AutoField(primary_key=True)
    childId = models.ForeignKey(birthRecord, on_delete=models.CASCADE, to_field='id')
    VaccineId = models.ForeignKey(vaccine, on_delete=models.CASCADE, to_field='id' )
    Description = models.CharField(max_length=200, null=True)
    vaccination_Time = models.CharField(max_length=100, null=True)
    RegisteredBy = models.CharField(max_length=150)

    class Meta:
        unique_together = (("childId", "VaccineId"),)


class feedback(models.Model):
    id = models.AutoField(primary_key=True)
    Feedback_msg = models.CharField(max_length=250)
    Father_Email = models.ForeignKey(Parent, on_delete=models.CASCADE, to_field='Father_Email')


class future_vaccines(models.Model):
    id = models.AutoField(primary_key=True)
    VaccineId = models.ForeignKey(vaccine, on_delete=models.CASCADE, to_field='id')
    child_id = models.ForeignKey(birthRecord, on_delete=models.CASCADE, to_field='id')
    Description = models.CharField(max_length=250)
    Date = models.CharField(max_length=100)
    HCW_Email = models.ForeignKey(healthcareworker, on_delete=models.CASCADE,to_field='Email', null=True)
    OS_Email = models.ForeignKey(OperatingStaff, on_delete=models.CASCADE,to_field='OS_Email')