from .views import *
from django.urls import path

urlpatterns = [
    path('sendsms/', SendSms.as_view()),
    path('registerper/', RegisterPerson.as_view()),
    path('checksms/', CheckSms.as_view()),
    path('GetPersonCategories/', GetPersonCategories.as_view()),
    path('justsms/', JustSms.as_view()),
    path('getallpersondetails/', GetAllPersonDetails.as_view()),
    path('getallcustomersdetails/', GetAllCustomersDetails.as_view()),
    path('getalltechniciansdetails/', GetAllTechniciansDetails.as_view()),
    # path('getpersondetails/', GetPersonDetails.as_view()),
    path('getcustomersdetails/', GetCustomersDetails.as_view()),
    path('gettechniciansdetails/', GetTechniciansDetails.as_view()),
    path('getpersonauth/', GetPersonAuth.as_view()),
    path('getallmembergroup/', GetAllMemberGroup.as_view()),
    path('registercompanymembers/', RegisterCompanyMembers.as_view()),
    path('getallcompanymemebers/', GetAllCompanyMembers.as_view()),
    path('getpersondetails/', GetPersonDetails.as_view()),
    path('editcompanymembers/', EditCompanyMembers.as_view()),
    path('deletecompanymember/', DeleteCompanyMember.as_view()),
    path('getallpermissions/', GetAllPermissions.as_view()),
    path('createmembergroup/', CreateMemberGroup.as_view()),
    path('editmembergroup/', EditMemberGroup.as_view()),
    path('deletemembersgroup/', DeleteMembersGroup.as_view()),
    path('createcustomeraddress/', CreateCustomerAddress.as_view()),
    path('editcustomeraddress/', EditCustomerAddress.as_view()),
    path('deletecustomeraddress/', DeleteCustomerAddress.as_view()),
    path('changepass/', changepass.as_view()),
    path('ForgetSendSms/', ForgetSendSms.as_view()),
    path('technicianuploadpic/', TechnicianUploadPic.as_view()),
    path('customeruploadpic/', CustomerUploadPic.as_view())
]