from django.db import IntegrityError
from django.shortcuts import render
from . models import *
from . serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# Create your views here.


class SIGNIN(APIView):
    def post(self,request):
        if request.method=='POST':
            data=request.POST.dict()
            email=data['email']
            hi=accesslevel.objects.filter(email=email).first()
            serializer=access(hi)
            if hi.password==data['password']:
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)

class savedirectorEPI(APIView):

        def post(self, request):
             
                        accessleve=accesslevel()
                        data = request.POST.dict()
                        serializer = DirectorEPISerializer(data=data)
                        email=data.get('directorEPIEmail')
                        password=data.get('directorEPIPassword')
                        access=data.get('access')
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
                        
        def get(self, request):
                    directorEP = directorEPI.objects.all().order_by('id')
                    serializer = DirectorEPISerializer(directorEP, many=True)
                    return Response(serializer.data)
                            
        def put(self, request):
            data = request.data
            try:
                director_ep = directorEPI.objects.get(id=data['id'])
                director_ep.directorEPIfullName = data.get('updatedirectorEPIfullName', director_ep.directorEPIfullName)
                director_ep.directorEPIEmail = data.get('updatedirectorEPIEmail', director_ep.directorEPIEmail)
                director_ep.directorEPIProvince = data.get('updatedirectorEPIProvince', director_ep.directorEPIProvince)
                director_ep.directorEPIphone = data.get('updatedirectorEPIphone', director_ep.directorEPIphone)
                director_ep.save()
                return Response(status=status.HTTP_200_OK)
            except directorEPI.DoesNotExist:
                print("Director EPI not found")
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                                   
class countdirectorEPI(APIView):
    def get(self, request):
        if request.method=='GET':
            directorEP = directorEPI.objects.count()
            return Response(directorEP)

        
        
class saveVaccineManager(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        accessleve=accesslevel()
                        data = request.POST.dict()
                        serializer = VaccineManagerSerializer(data=data)
                        email=data['VM_Email']
                        password=data['VM_Password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                vaccineManager = VaccineManager.objects.all().order_by('id')
                serializer = VaccineManagerSerializer(vaccineManager, many=True)

                return Response(serializer.data)
            
        def put(self, request):
            data = request.data
            try:
                VM = VaccineManager.objects.get(id=data['id'])
                VM.VM_FullName = data.get('VM_FullName', VM.VM_FullName)
                VM.VM_Email = data.get('VM_Email', VM.VM_Email)
                VM.province = data.get('province', VM.province)
                VM.phone = data.get('phone', VM.phone)
                VM.save()
                return Response(status=status.HTTP_200_OK)
            except VaccineManager.DoesNotExist:
                print("Vaccine Manager not found")
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class countvacM(APIView):

    def get(self, request):
        if request.method=='GET':
            vacm = VaccineManager.objects.count()
            return Response(vacm)
        

class savehospital(APIView):

        def post(self, request):
                    data = request.POST.dict()
                    serializer = HospitalSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(status=status.HTTP_200_OK)
                    else:
                        print(serializer.errors)
                        return Response(status=status.HTTP_404_NOT_FOUND)
                    
        def get(self, request):
            EP = hospital.objects.all().order_by('id')
            serializer = HospitalSerializer(EP, many=True)
            return Response(serializer.data)
        
        def put(self, request):
            data = request.data
            try:
                hosp = hospital.objects.get(id=data['id'])
                hosp.hospitalName = data.get('hospitalName', hosp.hospitalName)
                hosp.hospitalCity = data.get('hospitalCity', hosp.hospitalCity)
                hosp.hospitalProvince = data.get('hospitalProvince', hosp.hospitalProvince)
                hosp.hospitalAddress = data.get('hospitalAddress', hosp.hospitalAddress)
                hosp.save()
                return Response(status=status.HTTP_200_OK)
            except hospital.DoesNotExist:
                print("Hospital not found")
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class counthospital(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = hospital.objects.count()
            return Response(EP)
        
class savemedicalSuperIntendent(APIView):

        def post(self, request):
                        data = request.POST.dict()
                        accessleve=accesslevel()
                        serializer = medicalSuperIntendentSerializer(data=data)
                        email=data['medicalSuperIntendentEmail']
                        password=data['medicalSuperIntendentPassword']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)

        def get(self, request):
            if request.method=='GET':
                EP = medicalSuperIntendent.objects.all().order_by('id')
                serializer = medicalSuperIntendentSerializer(EP, many=True)
                return Response(serializer.data)
            
        def put(self, request):
            data = request.data
            try:
                MSI = medicalSuperIntendent.objects.get(id=data['id'])
                MSI.medicalSuperIntendentEmail = data.get('medicalSuperIntendentEmail', MSI.medicalSuperIntendentEmail)
                MSI.medicalSuperIntendentFullName = data.get('medicalSuperIntendentFullName', MSI.medicalSuperIntendentFullName)
                MSI.phone = data.get('phone', MSI.phone)
                MSI.save()
                return Response(status=status.HTTP_200_OK)
            except hospital.DoesNotExist:
                print("Medical Superintendent not found")
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class HospitalIdsView(APIView):
    def get(self, request):
        hospitals = hospital.objects.all().values('id', 'hospitalName')
        return Response(hospitals)
    

class countmedicalSuperIntendent(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = medicalSuperIntendent.objects.count()
            return Response(EP)
                                      
class savevaccine(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = vaccineSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
                            
        def get(self, request):
            if request.method=='GET':
                EP = vaccine.objects.all().order_by('id')
                serializer = vaccineSerializer(EP, many=True)
                return Response(serializer.data)

class countvaccine(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccine.objects.count()
            return Response(EP)

class getHospitalForDirectorEPI(APIView):
     def get(self, request):
        directorEP_email = request.query_params.get("directorEPIEmail")
        directorEP = directorEPI.objects.get(directorEPIEmail=directorEP_email)
        directorEPIProvince = directorEP.directorEPIProvince

        hospitals = hospital.objects.filter(hospitalProvince=directorEPIProvince)
        serializer = HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)
     
class countHospitalForDirectorEPI(APIView):

    def get(self, request):
        directorEP_email = request.query_params.get("directorEPIEmail")
        directorEP = directorEPI.objects.get(directorEPIEmail=directorEP_email)
        directorEPIProvince = directorEP.directorEPIProvince

        hospitals = hospital.objects.filter(hospitalProvince=directorEPIProvince).count()
        return Response(hospitals)
    

class DirectorEPI_IdsView(APIView):
    def get(self, request):
        depi = directorEPI.objects.all().values('id', 'directorEPIfullName')
        return Response(depi) 
    
class Vaccine_IdsView(APIView):
    def get(self, request):
        vac = vaccine.objects.all().values('id', 'vaccineName')
        return Response(vac) 

class saveAssignedVaccinesToDirectorEPI(APIView):

        def post(self, request):
                        data = request.data
                        serializer = VaccineAssignedToDirectorEPISerializer(data=data)
                        if serializer.is_valid():
                                serializer.save()
                                return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
                        
        def get(self, request):
                if request.method=='GET':
                    directorEP = VaccineAssignedToDirectorEPI.objects.select_related('assigned_vaccine_id').all().order_by('directorEPI_ID')
                    serializer = VaccineAssignedToDirectorEPISerializer(directorEP, many=True)
                    return Response(serializer.data)
        
        def put(self, request):
                data = request.data
                try:
                    directorEPI_ID = data.get('directorEPI_ID')
                    assigned_vaccine_id = data.get('assigned_vaccine_id')
                    vacAssigned = VaccineAssignedToDirectorEPI.objects.filter(
                        directorEPI_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    if vacAssigned.exists():
                        if vacAssigned.count() > 1:
                            print("Multiple objects returned for the given filter conditions")
                            print("Matching objects:")
                            for obj in vacAssigned:
                                print(obj)
                            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            vacAssigned = vacAssigned.first()
                            serializer = VaccineAssignedToDirectorEPISerializer(vacAssigned)
                            serialized_data = serializer.data
                            return Response(serialized_data)
                    else:
                        print("Director EPI not found")
                        return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                
class countVaccineAssignedToDirectorEPI(APIView):

    def get(self, request):
        if request.method=='GET':
            VaccineAssignedToDirectorEP = VaccineAssignedToDirectorEPI.objects.count()
            return Response(VaccineAssignedToDirectorEP)
                            

class saveVaccineAssignedToHospital(APIView):
        def post(self, request):             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = VaccineAssignedToHospitalSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
                if request.method=='GET':
                    directorEP = VaccineAssignedToHospital.objects.all().order_by('id')
                    serializer = VaccineAssignedToHospitalSerializer(directorEP, many=True)
                    return Response(serializer.data)
                
        def put(self, request):
                data = request.data
                try:
                    directorEPI_ID = data.get('Hospital_ID')
                    assigned_vaccine_id = data.get('assigned_vaccine_id')
                    vacAssigned = VaccineAssignedToHospital.objects.filter(
                        Hospital_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    if vacAssigned.exists():
                        if vacAssigned.count() > 1:
                            print("Multiple objects returned for the given filter conditions")
                            print("Matching objects:")
                            for obj in vacAssigned:
                                print(obj)
                            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            vacAssigned = vacAssigned.first()
                            serializer = VaccineAssignedToHospitalSerializer(vacAssigned)
                            serialized_data = serializer.data
                            return Response(serialized_data)
                    else:
                        print("Hospital not found")
                        return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class countVaccineAssignedToHospital(APIView):

    def get(self, request):
        if request.method=='GET':
            VaccineAssignedToDirectorEP = VaccineAssignedToHospital.objects.count()
            return Response(VaccineAssignedToDirectorEP)
        

class getProvinceOfDirectorEPI(APIView):
     def get(self, request):
        directorEP_email = request.query_params.get("directorEPIEmail")
        directorEP = directorEPI.objects.get(directorEPIEmail=directorEP_email)
        directorEPIProvince = directorEP.directorEPIProvince

        return Response(directorEPIProvince)
     
class saveHCWAdmin(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        accessleve=accesslevel()
                        data = request.POST.dict()
                        serializer = HealthCareWorkerAdminSerializer(data=data)
                        email=data['email']
                        password=data['password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                hcwAdmin = HealthCareWorkerAdmin.objects.all().order_by('id')
                serializer = HealthCareWorkerAdminSerializer(hcwAdmin, many=True)

                return Response(serializer.data)
            
        def put(self, request):
                data = request.data
                
                try:
                        i=data['id']
                        q = HealthCareWorkerAdmin.objects.get(id=i)
                        q.id=data['updateid']
                        q.save()
                        so= HealthCareWorkerAdmin.objects.get(id=i)
                        so.delete()
                        return Response(status=status.HTTP_200_OK)
                except:
                        print("id is not updating")
                        try:
                            i=data['id']
                            q = HealthCareWorkerAdmin.objects.get(id=i)
                            q.fullName=data['fullName']
                            q.save()
                            return Response(status=status.HTTP_200_OK)
                        except:
                            print("fullname is not updating")
                        try:
                                i=data['id']
                                q = HealthCareWorkerAdmin.objects.get(id=i)
                                q.email=data['email']
                                q.save()
                                return Response(status=status.HTTP_200_OK)
                        except:
                                    print("email is not updating")
                        try:
                                        i=data['id']
                                        q = HealthCareWorkerAdmin.objects.get(id=i)
                                        q.contact=data['contact']
                                        q.save()
                                        return Response(status=status.HTTP_200_OK)
                        except:
                                      print("contact is not updating")
                                      Response(status=status.HTTP_404_NOT_FOUND)

class countHCWA(APIView):

    def get(self, request):
        if request.method=='GET':
            vacm = HealthCareWorkerAdmin.objects.count()
            return Response(vacm)
        
class saveVaccineAssignedToHealthCareWorkerAdmin(APIView):
        def post(self, request):             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = VaccineAssignedToHealthCareWorkerAdminSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
                if request.method=='GET':
                    directorEP = VaccineAssignedToHealthCareWorkerAdmin.objects.select_related('assigned_vaccine_id').all().order_by('hcwAdminID')
                    serializer = VaccineAssignedToHealthCareWorkerAdminSerializer(directorEP, many=True)
                    return Response(serializer.data)
        
        def put(self, request):
                data = request.data
                try:
                    directorEPI_ID = data.get('hcwAdminID')
                    assigned_vaccine_id = data.get('assigned_vaccine_id')
                    vacAssigned = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(
                        hcwAdminID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    if vacAssigned.exists():
                        if vacAssigned.count() > 1:
                            print("Multiple objects returned for the given filter conditions")
                            print("Matching objects:")
                            for obj in vacAssigned:
                                print(obj)
                            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            vacAssigned = vacAssigned.first()
                            serializer = VaccineAssignedToHealthCareWorkerAdminSerializer(vacAssigned)
                            serialized_data = serializer.data
                            return Response(serialized_data)
                    else:
                        print("HCWA not found")
                        return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class countVaccineAssignedToHealthCareWorkerAdmin(APIView):

    def get(self, request):
        if request.method=='GET':
            VaccineAssignedToDirectorEP = VaccineAssignedToHealthCareWorkerAdmin.objects.count()
            return Response(VaccineAssignedToDirectorEP)
        
class getRegionOf_HCWA(APIView):
     def get(self, request):
        email = request.query_params.get("email")
        directorEP = HealthCareWorkerAdmin.objects.get(email=email)
        hcwa_region = directorEP.region

        return Response(hcwa_region)

class savehealthcareworker(APIView):
        def post(self, request):
                if request.method=="POST": 
                        data = request.POST.dict()
                        accessleve=accesslevel()
                        serializer = healthcareworkerSerializer(data=data)
                        email=data['Email']
                        password=data['Password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                EP = healthcareworker.objects.all().order_by('id')
                serializer = healthcareworkerSerializer(EP, many=True)

                return Response(serializer.data)

class counthealthcareworker(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = healthcareworker.objects.count()
            return Response(EP)

class saveVaccineAssignedToHCW(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = vaccineAssignedToHCWSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                EP = vaccineAssignedToHCW.objects.all().order_by('id')
                serializer = vaccineAssignedToHCWSerializer(EP, many=True)

                return Response(serializer.data)
            
        def put(self, request):
                data = request.data
                try:
                    directorEPI_ID = data.get('HCW_ID')
                    assigned_vaccine_id = data.get('assigned_vaccine_id')
                    vacAssigned = vaccineAssignedToHCW.objects.filter(
                        HCW_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    if vacAssigned.exists():
                        if vacAssigned.count() > 1:
                            print("Multiple objects returned for the given filter conditions")
                            print("Matching objects:")
                            for obj in vacAssigned:
                                print(obj)
                            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            vacAssigned = vacAssigned.first()
                            serializer = vaccineAssignedToHCWSerializer(vacAssigned)
                            serialized_data = serializer.data
                            return Response(serialized_data)
                    else:
                        print("HCW not found")
                        return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class countVaccineAssignedToHCW(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccineAssignedToHCW.objects.count()
            return Response(EP)
        
class getRegionOfHCWA(APIView):
     def get(self, request):
        HCWA_Email = request.query_params.get("email")
        HCWA = HealthCareWorkerAdmin.objects.get(region=HCWA_Email)
        HCWA_Region = HCWA.region

        hcw = healthcareworker.objects.filter(region=HCWA_Region)
        serializer = healthcareworkerSerializer(hcw, many=True)
        return Response(serializer.data)
     
# class get_HCW_For_HCWA(APIView):
#      def get(self, request):
#         region = request.query_params.get("region")
#         hcw = healthcareworker.objects.get(region=region)
#         hcw_region = hcw.region

#         healthcareworkers = healthcareworker.objects.filter(region=hcw_region)
#         serializer = healthcareworkerSerializer(healthcareworkers, many=True)
#         return Response(serializer.data)
     
class getHospitalIDofMSI(APIView):
     def get(self, request):
        msi_email = request.query_params.get("msi_email")
        msi = medicalSuperIntendent.objects.get(medicalSuperIntendentEmail=msi_email)
        msiHospital = msi.hospitalID
        serializer = HospitalSerializer(msiHospital)
        return Response(serializer.data)
     
class saveOperatingStaff(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        accessleve=accesslevel()
                        data = request.POST.dict()
                        serializer = OperatingStaffSerializer(data=data)
                        email=data['OS_Email']
                        password=data['OS_Password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                vaccineManager = OperatingStaff.objects.all().order_by('id')
                serializer = OperatingStaffSerializer(vaccineManager, many=True)

                return Response(serializer.data)
            
        def put(self, request):
                data = request.data
                
                try:
                        i=data['id']
                        q = OperatingStaff.objects.get(id=i)
                        q.id=data['updateid']
                        q.save()
                        so= OperatingStaff.objects.get(id=i)
                        so.delete()
                        return Response(status=status.HTTP_200_OK)
                except:
                        print("id is not updating")
                        try:
                            i=data['id']
                            q = OperatingStaff.objects.get(id=i)
                            q.OS_fullName=data['OS_fullName']
                            q.save()
                            return Response(status=status.HTTP_200_OK)
                        except:
                            print("OS_FullName is not updating")
                        try:
                                i=data['id']
                                q = OperatingStaff.objects.get(id=i)
                                q.OS_Email=data['OS_Email']
                                q.save()
                                return Response(status=status.HTTP_200_OK)
                        except:
                                    print("OS_Email is not updating")
                                    try:
                                        i=data['id']
                                        q = OperatingStaff.objects.get(id=i)
                                        q.OS_Contact=data['OS_Contact']
                                        q.save()
                                        return Response(status=status.HTTP_200_OK)
                                    except:
                                     print("OS_Contact is not updating")
                                     try:
                                        i=data['id']
                                        q = OperatingStaff.objects.get(id=i)
                                        q.OS_Password=data['OS_Password']
                                        q.save()
                                        return Response(status=status.HTTP_200_OK)
                                     except:
                                      print("Password is not updating")
                                      Response(status=status.HTTP_404_NOT_FOUND)

class countOperatingStaff(APIView):

    def get(self, request):
        if request.method=='GET':
            VaccineAssignedToDirectorEP = OperatingStaff.objects.count()
            return Response(VaccineAssignedToDirectorEP)
        

class saveParent(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        accessleve=accesslevel()
                        data = request.POST.dict()
                        serializer = ParentSerializer(data=data)
                        email=data['Father_Email']
                        password=data['Password']
                        access=data['access']
                        accessleve.email=email
                        accessleve.password=password
                        accessleve.access=access
                        if serializer.is_valid():
                            serializer.save()
                            accessleve.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                parent = Parent.objects.all().order_by('id')
                serializer = ParentSerializer(parent, many=True)

                return Response(serializer.data)
            
class saveBirthRecord(APIView):

        def post(self, request):
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = birthRecordSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        def get(self, request):
            if request.method=='GET':
                EP = birthRecord.objects.all().order_by('id')
                serializer = birthRecordSerializer(EP, many=True)
                return Response(serializer.data)

class countBirthRecord(APIView):
    def get(self, request):
        if request.method=='GET':
            EP = birthRecord.objects.count()
            return Response(EP)

        
class savevaccineRecord(APIView):

        def post(self, request):
             
                if request.method=="POST": 
                        data = request.POST.dict()
                        serializer = vaccineRecordSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            child_id = serializer.validated_data.get('childId')
                            vaccine_id = serializer.validated_data.get('VaccineId')
                            future_vaccines.objects.filter(child_id=child_id, VaccineId=vaccine_id).delete()
                        hospital_id = data.get('hospital_id')  # Assuming you have hospital_id in the request data
                        vaccine_id = serializer.data.get('VaccineId')  # Assuming you have vaccine_id in the serializer response data
                        HCWA_Email = data.get('HCWA_Email')
                        try:
                            vaccine_assigned = VaccineAssignedToHospital.objects.get(Hospital_ID=hospital_id, assigned_vaccine_id=vaccine_id)
                            vaccine_assigned.Vaccine_Quantity -= 1
                            vaccine_assigned.save()
                        except VaccineAssignedToHospital.DoesNotExist:
                            HCW_ID = healthcareworker.objects.get(Email=HCWA_Email)
                            hcw_id = HCW_ID.id
                            vaccine_assigned = vaccineAssignedToHCW.objects.get(HCW_ID=hcw_id, assigned_vaccine_id=vaccine_id)
                            vaccine_assigned.Vaccine_Quantity -= 1
                            vaccine_assigned.save()

                        return Response(status=status.HTTP_200_OK)
                else:
                        print(serializer.errors)
                        return Response(status=status.HTTP_404_NOT_FOUND)
                        
        def get(self, request):
                if request.method=='GET':
                    EP = vaccineRecord.objects.all().order_by('id')
                    serializer = vaccineRecordSerializer(EP, many=True)
                    return Response(serializer.data)
    

class countvaccineRecord(APIView):

    def get(self, request):
        if request.method=='GET':
            EP = vaccineRecord.objects.count()
            return Response(EP)
        
class getParentEmail(APIView):
     def get(self, request):
        parent_Email = request.query_params.get("Father_Email")
        try:
            parent = Parent.objects.get(Father_Email=parent_Email)
            # serializer = ParentSerializer(parent)
            return Response({'exists': True})
        except Parent.DoesNotExist:
            return Response({'exists': False})
                                    

class getDEPIforVM(APIView):
     def get(self, request):
        vm_email = request.query_params.get("VM_Email")
        vm = VaccineManager.objects.get(VM_Email=vm_email)
        VaccineManager_Province = vm.province

        DEPIs = directorEPI.objects.filter(directorEPIProvince=VaccineManager_Province)
        count = DEPIs.count()

        serializer = DirectorEPISerializer(DEPIs, many=True)
        response_data = {
            'count': count,
            'depis': serializer.data
        }
        return Response(response_data)
     

class CheckAssignmentView(APIView):
    def get(self, request):
        assigned_vaccine_id = request.GET.get('assigned_vaccine_id')
        directorEPI_ID = request.GET.get('directorEPI_ID')

        if assigned_vaccine_id is None or directorEPI_ID is None:
            return Response({'error': 'assigned_vaccine_id and directorEPI_ID parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        assignment_exists = VaccineAssignedToDirectorEPI.objects.filter(
            assigned_vaccine_id=assigned_vaccine_id,
            directorEPI_ID=directorEPI_ID
        ).exists()
        return Response({'assignment_exists': assignment_exists}, status=status.HTTP_200_OK)
    

class getVacForVM(APIView):
     def get(self, request):
        vacc = request.query_params.get("assigned_vaccine_id")
        vac = vaccine.objects.get(id=vacc)
        v = vac.id
        vaccines = vaccine.objects.filter(id=v)
        serializer = vaccineSerializer(vaccines, many=True)
        return Response(serializer.data)
     

class updatingVacQuantity(APIView):
    def put(self, request):
                data = request.data
                directorEPI_ID = data.get('directorEPI_ID')
                assigned_vaccine_id = data.get('assigned_vaccine_id')
                new_quantity = data.get('newQuantity')
                old_quantity = data.get('oldQuantity')
                try:
                    directorEP = VaccineAssignedToDirectorEPI.objects.get(
                        directorEPI_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    directorEP.Vaccine_Quantity = new_quantity
                    directorEP.save()

                    vac = vaccine.objects.get(id = assigned_vaccine_id)
                    vac.vaccinequantity = old_quantity
                    vac.save()


                    return Response(status=status.HTTP_200_OK)
                except directorEPI.DoesNotExist:
                    print("Director EPI not found")
                    return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

class getVaccinesForDEPI(APIView):
    def get(self, request):
        depi_Email = request.query_params.get("DEPI_Email")
        try:
            depi = directorEPI.objects.get(directorEPIEmail=depi_Email)
            depi_id = depi.id
            vaccines = VaccineAssignedToDirectorEPI.objects.filter(directorEPI_ID=depi_id)
            serializer = VaccineAssignedToDirectorEPISerializer(vaccines, many=True)
            return Response(serializer.data)
        except directorEPI.DoesNotExist:
            print("Director EPI not found")
            return Response(status=status.HTTP_404_NOT_FOUND)
        except VaccineAssignedToDirectorEPI.DoesNotExist:
            print("VaccineAssignedToDirectorEPI not found")
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CheckAssignmentViewForHospital(APIView):
    def get(self, request):
        assigned_vaccine_id = request.GET.get('assigned_vaccine_id')
        Hospital_ID = request.GET.get('Hospital_ID')

        if assigned_vaccine_id is None or Hospital_ID is None:
            return Response({'error': 'assigned_vaccine_id and Hospital_ID parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        assignment_exists = VaccineAssignedToHospital.objects.filter(
            assigned_vaccine_id=assigned_vaccine_id,
            Hospital_ID=Hospital_ID
        ).exists()
        return Response({'assignment_exists': assignment_exists}, status=status.HTTP_200_OK)


class getVacForDEPI(APIView):
    def get(self, request):
        vacc = request.query_params.get("assigned_vaccine_id")
        depiEmail = request.query_params.get("directorEPIEmail")
        depi = directorEPI.objects.get(directorEPIEmail=depiEmail)
        depi_id = depi.id
        vac = VaccineAssignedToDirectorEPI.objects.filter(assigned_vaccine_id=vacc, directorEPI_ID=depi_id)
        vac_ids = vac.values_list('id', flat=True)
        vaccines = VaccineAssignedToDirectorEPI.objects.filter(id__in=vac_ids)
        serializer = VaccineAssignedToDirectorEPISerializer(vaccines, many=True)
        return Response(serializer.data)


class updatingVacQuantityForHospital(APIView):
    def put(self, request):
                data = request.data
                directorEPI_ID = data.get('Hospital_ID')
                assigned_vaccine_id = data.get('assigned_vaccine_id')
                new_quantity = data.get('newQuantity')
                old_quantity = data.get('oldQuantity')
                try:
                    directorEP = VaccineAssignedToHospital.objects.get(
                        Hospital_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    directorEP.Vaccine_Quantity = new_quantity
                    directorEP.save()

                    vac = VaccineAssignedToDirectorEPI.objects.get(assigned_vaccine_id = assigned_vaccine_id)
                    vac.Vaccine_Quantity = old_quantity
                    vac.save()


                    return Response(status=status.HTTP_200_OK)
                except VaccineAssignedToHospital.DoesNotExist:
                    print("Hospital not found")
                    return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class CheckAssignmentViewForHCWA(APIView):
    def get(self, request):
        assigned_vaccine_id = request.GET.get('assigned_vaccine_id')
        HCWA_ID = request.GET.get('HCWA_ID')

        if assigned_vaccine_id is None or HCWA_ID is None:
            return Response({'error': 'assigned_vaccine_id and HCWA_ID parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        assignment_exists = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(
            assigned_vaccine_id=assigned_vaccine_id,
            hcwAdminID=HCWA_ID
        ).exists()
        return Response({'assignment_exists': assignment_exists}, status=status.HTTP_200_OK)


class updatingVacQuantityForHCWA(APIView):
    def put(self, request):
                data = request.data
                directorEPI_ID = data.get('hcwAdminID')
                assigned_vaccine_id = data.get('assigned_vaccine_id')
                new_quantity = data.get('newQuantity')
                old_quantity = data.get('oldQuantity')
                try:
                    directorEP = VaccineAssignedToHealthCareWorkerAdmin.objects.get(
                        hcwAdminID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    directorEP.Vaccine_Quantity = new_quantity
                    directorEP.save()

                    vac = VaccineAssignedToDirectorEPI.objects.get(assigned_vaccine_id = assigned_vaccine_id)
                    vac.Vaccine_Quantity = old_quantity
                    vac.save()


                    return Response(status=status.HTTP_200_OK)
                except VaccineAssignedToHealthCareWorkerAdmin.DoesNotExist:
                    print("HCWA not found")
                    return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckAssignmentViewForHCW(APIView):
    def get(self, request):
        assigned_vaccine_id = request.GET.get('assigned_vaccine_id')
        HCW_ID = request.GET.get('HCW_ID')

        if assigned_vaccine_id is None or HCW_ID is None:
            return Response({'error': 'assigned_vaccine_id and HCW_ID parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        assignment_exists = vaccineAssignedToHCW.objects.filter(
            assigned_vaccine_id=assigned_vaccine_id,
            HCW_ID=HCW_ID
        ).exists()
        return Response({'assignment_exists': assignment_exists}, status=status.HTTP_200_OK)
    
class getVacForHCWA(APIView):
    def get(self, request):
        vacc = request.query_params.get("assigned_vaccine_id")
        depiEmail = request.query_params.get("HCWA_Email")
        depi = HealthCareWorkerAdmin.objects.get(email=depiEmail)
        depi_id = depi.id
        vac = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(assigned_vaccine_id=vacc, hcwAdminID=depi_id)
        vac_ids = vac.values_list('id', flat=True)
        vaccines = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(id__in=vac_ids)
        serializer = VaccineAssignedToHealthCareWorkerAdminSerializer(vaccines, many=True)
        return Response(serializer.data)
    

class updatingVacQuantityForHCW(APIView):
    def put(self, request):
                data = request.data
                directorEPI_ID = data.get('HCW_ID')
                assigned_vaccine_id = data.get('assigned_vaccine_id')
                new_quantity = data.get('newQuantity')
                old_quantity = data.get('oldQuantity')
                try:
                    directorEP = vaccineAssignedToHCW.objects.get(
                        HCW_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )
                    directorEP.Vaccine_Quantity = new_quantity
                    directorEP.save()

                    vac = VaccineAssignedToHealthCareWorkerAdmin.objects.get(assigned_vaccine_id = assigned_vaccine_id)
                    vac.Vaccine_Quantity = old_quantity
                    vac.save()


                    return Response(status=status.HTTP_200_OK)
                except vaccineAssignedToHCW.DoesNotExist:
                    print("HCW not found")
                    return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class getHospitalIDofOS(APIView):
     def get(self, request):
        msi_email = request.query_params.get("OS_Email")
        msi = OperatingStaff.objects.get(OS_Email=msi_email)
        msiHospital = msi.Hospital_ID
        serializer = HospitalSerializer(msiHospital)
        return Response(serializer.data)
     

class CheckAssignmentViewForOSbirthRecord(APIView):
    def get(self, request):
        assigned_vaccine_id = request.GET.get('assigned_vaccine_id')
        HCW_ID = request.GET.get('Hospital_ID')

        if assigned_vaccine_id is None or HCW_ID is None:
            return Response({'error': 'assigned_vaccine_id and Hospital_ID parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        assignment_exists = VaccineAssignedToHospital.objects.filter(
            assigned_vaccine_id=assigned_vaccine_id,
            Hospital_ID=HCW_ID
        ).exists()
        return Response({'assignment_exists': assignment_exists}, status=status.HTTP_200_OK)
    

class getVacForHospital(APIView):
    def get(self, request):
        vacc = request.query_params.get("assigned_vaccine_id")
        depiEmail = request.query_params.get("Hospital_ID")
        depi = VaccineAssignedToHospital.objects.get(Hospital_ID=depiEmail, assigned_vaccine_id = vacc)
        depi_id = depi.id
        vac = VaccineAssignedToHospital.objects.filter(assigned_vaccine_id=vacc, Hospital_ID=depi_id)
        vac_ids = vac.values_list('id', flat=True)
        vaccines = VaccineAssignedToHospital.objects.filter(id__in=vac_ids)
        serializer = VaccineAssignedToHospitalSerializer(vaccines, many=True)
        return Response(serializer.data)
    

class updatingVacQuantityForBirthRecordOS(APIView):
    def put(self, request):
                data = request.data
                directorEPI_ID = data.get('Hospital_ID')
                assigned_vaccine_id = data.get('assigned_vaccine_id')
                old_quantity = data.get('oldQuantity')
                try:
                    hosp = VaccineAssignedToHospital.objects.get(
                        Hospital_ID=directorEPI_ID,
                        assigned_vaccine_id=assigned_vaccine_id
                    )

                    hosp.Vaccine_Quantity = old_quantity
                    hosp.save()


                    return Response(status=status.HTTP_200_OK)
                except VaccineAssignedToHospital.DoesNotExist:
                    print("Hospital not found")
                    return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class getVaccQuantityOfHosp(APIView):
     def get(self, request):
        hospital_id = request.query_params.get("Hospital_ID")
        vac = request.query_params.get("assigned_vaccine_id")
        msi = VaccineAssignedToHospital.objects.get(Hospital_ID=hospital_id, assigned_vaccine_id=vac)
        serializer = VaccineAssignedToHospitalSerializer(msi)
        return Response(serializer.data)
     

class RetrieveOperatingStaff(APIView):
    def get(self, request):
        try:
            operating_staff_emails = OperatingStaff.objects.values_list('OS_Email', flat=True)
            birth_records = birthRecord.objects.filter(RegisteredBy__in=operating_staff_emails)
            
            # You can access the birth_records queryset and iterate over the objects
            # For example, you can access birth_records[0].fullName, birth_records[1].Gender, etc.
            
            # Return the serialized birth_records data in the response
            serializer = birthRecordSerializer(birth_records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except birthRecord.DoesNotExist:
            return Response("Birth Records not found", status=status.HTTP_404_NOT_FOUND)
        
        except OperatingStaff.DoesNotExist:
            return Response("Operating Staff not found", status=status.HTTP_404_NOT_FOUND)

        

class saveFeedback(APIView):

        def post(self, request):
                        data = request.POST.dict()
                        serializer = FeedbackSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
                        
        def get(self, request):
                    directorEP = feedback.objects.all().order_by('id')
                    serializer = FeedbackSerializer(directorEP, many=True)
                    return Response(serializer.data)
        

class getPare(APIView):

    def get(self, request):
                hospitals = hospital.objects.count()
                Vaccinemanager=VaccineManager.objects.count()
                directorEP=directorEPI.objects.count()
                medicalSuperIntenden=medicalSuperIntendent.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'hospitals','y':hospitals},{'x':'Vaccinemanager','y':Vaccinemanager},{'x':'directorEP','y':directorEP},{'x':'medicalSuperIntenden','y':medicalSuperIntenden}]
                    })
                print(data)
                return Response(data)

class dpidashboard(APIView):

    def get(self, request):
                hospitals = hospital.objects.count()
                VaccineAssignedToHospitals=VaccineAssignedToHospital.objects.count()
                HealthCareWorkerAdmins=HealthCareWorkerAdmin.objects.count()
                VaccineAssignedToHealthCareWorkerAdmins=VaccineAssignedToHealthCareWorkerAdmin.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'hospitals','y':hospitals},{'x':'VaccineAssignedToHospital','y':VaccineAssignedToHospitals},{'x':'HealthCareWorkerAdmin','y':HealthCareWorkerAdmins},{'x':'VaccineAssignedToHealthCareWorkerAdmin','y':VaccineAssignedToHealthCareWorkerAdmins}]
                    })
                print(data)
                return Response(data)

class Vmdashboard(APIView):

    def get(self, request):
                hospitals = vaccine.objects.count()
                VaccineAssignedToHospitals=directorEPI.objects.count()
                HealthCareWorkerAdmins=VaccineAssignedToDirectorEPI.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'vaccine','y':hospitals},{'x':'directorEPI','y':VaccineAssignedToHospitals},{'x':'VaccineAssignedToDirectorEPI','y':HealthCareWorkerAdmins}]
                    })
                print(data)
                return Response(data)


class HCWAdashboard(APIView):

    def get(self, request):
                hospitals = VaccineAssignedToHealthCareWorkerAdmin.objects.count()
                VaccineAssignedToHospitals=healthcareworker.objects.count()
                HealthCareWorkerAdmins=vaccineAssignedToHCW.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'VaccineAssignedToHealthCareWorkerAdmin','y':hospitals},{'x':'healthcareworker','y':VaccineAssignedToHospitals},{'x':'vaccineAssignedToHCW','y':HealthCareWorkerAdmins}]
                    })
                print(data)
                return Response(data)

class MSIAdashboard(APIView):

    def get(self, request):
                hospitals = VaccineAssignedToHospital.objects.count()
                VaccineAssignedToHospitals=OperatingStaff.objects.count()
                HealthCareWorkerAdmins=birthRecord.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'VaccineAssignedToHospital','y':hospitals},{'x':'OperatingStaff','y':VaccineAssignedToHospitals},{'x':'birthRecord','y':HealthCareWorkerAdmins}]
                    })
                print(data)
                return Response(data)


class HCWAdashboard(APIView):

    def get(self, request):
                hospitals = vaccineAssignedToHCW.objects.count()
                VaccineAssignedToHospitals=vaccineRecord.objects.count()
                HealthCareWorkerAdmins=birthRecord.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'vaccineAssignedToHCW','y':hospitals},{'x':'vaccineRecord','y':VaccineAssignedToHospitals},{'x':'birthRecord','y':HealthCareWorkerAdmins}]
                    })
                print(data)
                return Response(data)


class OPdashboard(APIView):

    def get(self, request):
                hospitals = VaccineAssignedToHospital.objects.count()
                VaccineAssignedToHospitals=vaccineRecord.objects.count()
                HealthCareWorkerAdmins=birthRecord.objects.count()
                data = []

                data.append({
                        'id': 'Data',
                        'data': [{'x':'VaccineAssignedToHospital','y':hospitals},{'x':'vaccineRecord','y':VaccineAssignedToHospitals},{'x':'birthRecord','y':HealthCareWorkerAdmins}]
                    })
                print(data)
                return Response(data)
    
class getBirthRecordsforParent(APIView):
     def get(self, request):
        vm_email = request.query_params.get("Parent_Email")
        vm = Parent.objects.get(Father_Email=vm_email)
        Father_CNIC = vm.id

        br = birthRecord.objects.filter(Father_CNIC=Father_CNIC)
        count = br.count()

        serializer = birthRecordSerializer(br, many=True)
        response_data = {
            'count': count,
            'birthRecords': serializer.data
        }
        return Response(response_data)
     

class getVaccineRecordsforParent(APIView):
    def get(self, request):
        parent_email = request.GET.get('Parent_Email', None)
        if parent_email is None:
            return JsonResponse({'error': 'Parent_Email parameter is missing'}, status=400)

        try:
            parent = Parent.objects.get(Father_Email=parent_email)
        except Parent.DoesNotExist:
            return JsonResponse({'error': 'Parent not found'}, status=404)

        child_ids = birthRecord.objects.filter(Father_CNIC=parent.id).values_list('id', flat=True)
        vaccine_records = vaccineRecord.objects.filter(childId__in=child_ids)
        count = vaccine_records.count()

        serializer = vaccineRecordSerializer(vaccine_records, many=True)
        response_data = {
            'count': count,
            'vaccine_records': serializer.data
        }
        return Response(response_data)

class getVaccineAssignedToHospitalForOS(APIView):
    def get(self, request):
        os_email = request.GET.get('OS_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'OS_Email parameter is missing'}, status=400)

        try:
            operating_staff = OperatingStaff.objects.get(OS_Email=os_email)
        except OperatingStaff.DoesNotExist:
            return JsonResponse({'error': 'Operating Staff not found'}, status=404)

        assigned_vaccines = VaccineAssignedToHospital.objects.filter(Hospital_ID=operating_staff.Hospital_ID)

        total_assigned_vaccines = assigned_vaccines.count()

        serializer = VaccineAssignedToHospitalSerializer(assigned_vaccines, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'vaccine_records': serializer.data
        }
        return Response(response_data)


class getVaccineAssignedToHCWA(APIView):
    def get(self, request):
        os_email = request.GET.get('HCWA_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'HCWA_Email parameter is missing'}, status=400)

        try:
            operating_staff = HealthCareWorkerAdmin.objects.get(email=os_email)
        except HealthCareWorkerAdmin.DoesNotExist:
            return JsonResponse({'error': 'HCWA not found'}, status=404)

        assigned_vaccines = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(hcwAdminID=operating_staff.id)

        total_assigned_vaccines = assigned_vaccines.count()

        serializer = VaccineAssignedToHealthCareWorkerAdminSerializer(assigned_vaccines, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'vaccine_records': serializer.data
        }
        return Response(response_data)
    
class getVaccineAssignedToHCW(APIView):
    def get(self, request):
        os_email = request.GET.get('HCW_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'HCW_Email parameter is missing'}, status=400)

        try:
            operating_staff = healthcareworker.objects.get(Email=os_email)
        except healthcareworker.DoesNotExist:
            return JsonResponse({'error': 'HCW not found'}, status=404)

        assigned_vaccines = vaccineAssignedToHCW.objects.filter(HCW_ID=operating_staff.id)

        total_assigned_vaccines = assigned_vaccines.count()

        serializer = vaccineAssignedToHCWSerializer(assigned_vaccines, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'vaccine_records': serializer.data
        }
        return Response(response_data)


class getVaccinesAssignedToHCWA_ForDEPI(APIView):
    def get(self, request):
        os_email = request.GET.get('DEPI_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'DEPI_Email parameter is missing'}, status=400)

        try:
            operating_staff = VaccineAssignedToHealthCareWorkerAdmin.objects.filter(directorEPI_Email=os_email)
        except VaccineAssignedToHealthCareWorkerAdmin.DoesNotExist:
            return JsonResponse({'error': 'Vaccine Assigned not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = VaccineAssignedToHealthCareWorkerAdminSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'vaccine_records': serializer.data
        }
        return Response(response_data)


class getHCWA_ForDEPI(APIView):
    def get(self, request):
        os_email = request.GET.get('DEPI_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'DEPI_Email parameter is missing'}, status=400)

        try:
            operating_staff = HealthCareWorkerAdmin.objects.filter(directorEPI_Email=os_email)
        except HealthCareWorkerAdmin.DoesNotExist:
            return JsonResponse({'error': 'Vaccine Assigned not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = HealthCareWorkerAdminSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'HCWA': serializer.data
        }
        return Response(response_data)
    
class getVaccinesAssignedToHospital(APIView):
    def get(self, request):
        os_email = request.GET.get('DEPI_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'DEPI_Email parameter is missing'}, status=400)

        try:
            operating_staff = VaccineAssignedToHospital.objects.filter(DirectorEPI_Email=os_email)
        except VaccineAssignedToHospital.DoesNotExist:
            return JsonResponse({'error': 'Vaccine Assigned not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = VaccineAssignedToHospitalSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'hospital': serializer.data
        }
        return Response(response_data)
    
class getHCWforHCWA(APIView):
    def get(self, request):
        os_email = request.GET.get('HCWA_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'HCWA_Email parameter is missing'}, status=400)

        try:
            operating_staff = healthcareworker.objects.filter(HCWA_Email=os_email)
        except healthcareworker.DoesNotExist:
            return JsonResponse({'error': 'Vaccine Assigned not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = healthcareworkerSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'hcw': serializer.data
        }
        return Response(response_data)


class getVaccAssignedToHCWforHCWA(APIView):
    def get(self, request):
        os_email = request.GET.get('HCWA_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'HCWA_Email parameter is missing'}, status=400)

        try:
            operating_staff = vaccineAssignedToHCW.objects.filter(HCWA_Email=os_email)
        except vaccineAssignedToHCW.DoesNotExist:
            return JsonResponse({'error': 'Vaccine Assigned not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = vaccineAssignedToHCWSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'vaccine_records': serializer.data
        }
        return Response(response_data)
    
class getVaccAssignedToMSI(APIView):
    def get(self, request):
        os_email = request.GET.get('MSI_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'MSI_Email parameter is missing'}, status=400)

        try:
            operating_staff = medicalSuperIntendent.objects.get(medicalSuperIntendentEmail=os_email)
            hospID = operating_staff.hospitalID
        except medicalSuperIntendent.DoesNotExist:
            return JsonResponse({'error': 'medicalSuperIntendent not found'}, status=404)

        hospital = VaccineAssignedToHospital.objects.filter(Hospital_ID=hospID)
        total_assigned_vaccines = hospital.count()

        serializer = VaccineAssignedToHospitalSerializer(hospital, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'vaccine_records': serializer.data
        }
        return Response(response_data)
    
class RetrieveBirthRecordsForMSI(APIView):
    def get(self, request):
        os_email = request.GET.get('MSI_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'MSI_Email parameter is missing'}, status=400)

        try:
            operating_staff = medicalSuperIntendent.objects.get(medicalSuperIntendentEmail=os_email)
            hospID = operating_staff.hospitalID
        except medicalSuperIntendent.DoesNotExist:
            return JsonResponse({'error': 'medicalSuperIntendent not found'}, status=404)

        birth_records = birthRecord.objects.filter(Hospital_ID=hospID.id)
        # birth_records = hospital.objects.filter(id=hospID.id)
        total_assigned_vaccines = birth_records.count()

        serializer = birthRecordSerializer(birth_records, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'birth_records': serializer.data
        }
        return Response(response_data)
    

class RetrieveOperatingStaffForMSI(APIView):
    def get(self, request):
        os_email = request.GET.get('MSI_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'MSI_Email parameter is missing'}, status=400)

        try:
            operating_staff = OperatingStaff.objects.filter(MSI_Email=os_email)
        except OperatingStaff.DoesNotExist:
            return JsonResponse({'error': 'medicalSuperIntendent not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = OperatingStaffSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'operating_staff': serializer.data
        }
        return Response(response_data)


class vaccinesForHCW(APIView):
    def get(self, request):
        os_email = request.GET.get('HCW_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'HCW_Email parameter is missing'}, status=400)

        try:
            operating_staff = healthcareworker.objects.get(Email=os_email)
        except healthcareworker.DoesNotExist:
            return JsonResponse({'error': 'healthcareworker not found'}, status=404)

        HCW_ID = operating_staff.id
        vaccineassigned = vaccineAssignedToHCW.objects.filter(HCW_ID=HCW_ID)
        total_assigned_vaccines = vaccineassigned.count()

        serializer = vaccineAssignedToHCWSerializer(vaccineassigned, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'records': serializer.data
        }
        return Response(response_data)
    

class saveFutureVaccines(APIView):
        def post(self, request):
                        data = request.POST.dict()
                        serializer = future_vaccinesSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(status=status.HTTP_200_OK)
                        else:
                            print(serializer.errors)
                            return Response(status=status.HTTP_404_NOT_FOUND)
        
        def get(self, request):
                    directorEP = future_vaccines.objects.all().order_by('id')
                    serializer = future_vaccinesSerializer(directorEP, many=True)
                    return Response(serializer.data)
        

class GetFutureVaccinesForHCW(APIView):
    def get(self, request):
        os_email = request.GET.get('HCW_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'HCW_Email parameter is missing'}, status=400)

        try:
            operating_staff = future_vaccines.objects.filter(HCW_Email=os_email)
        except healthcareworker.DoesNotExist:
            return JsonResponse({'error': 'healthcareworker not found'}, status=404)

        total_assigned_vaccines = operating_staff.count()

        serializer = future_vaccinesSerializer(operating_staff, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'records': serializer.data
        }
        return Response(response_data)
    

class CountFutureVaccines(APIView):
    def get(self, request):
        operating_staff = future_vaccines.objects.count()
        return Response(operating_staff)
    

class GetFutureVaccinesForParent(APIView):
    def get(self, request):
        os_email = request.GET.get('Parent_Email', None)
        if os_email is None:
            return JsonResponse({'error': 'Parent_Email parameter is missing'}, status=400)

        try:
            parent = Parent.objects.get(Father_Email=os_email)
            parentID = parent.id
            operating_staff = birthRecord.objects.get(Father_CNIC=parentID)
        except birthRecord.DoesNotExist:
            return JsonResponse({'error': 'birthRecord not found'}, status=404)

        childID = operating_staff.id
        future_vac_records = future_vaccines.objects.filter(child_id=childID)
        total_assigned_vaccines = future_vac_records.count()

        serializer = future_vaccinesSerializer(future_vac_records, many=True)
        response_data = {
            'count': total_assigned_vaccines,
            'records': serializer.data
        }
        return Response(response_data)