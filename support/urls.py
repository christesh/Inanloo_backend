from .views import *
from django.urls import path

urlpatterns = [
    path('getuserchatstatus/', GetUserChatStatus.as_view()),
    path('getusermessages/', GetUserMessages.as_view()),
    path('sendmessages/', SendMessages.as_view()),
    path('setactiveuser/', SetActiveUser.as_view()),
    path('setdeactiveuser/', SetDeactiveUser.as_view()),
    path('connectedusers/', ConnectedUsers.as_view()),
    path('getdatetimenow/', GetDateTimeNow.as_view()),
    path('createticket/', Createticket.as_view()),
    path('getticketallstatusprioritysubject/', GetTicketAllStatusPrioritySubject.as_view()),
    path('uploadticketfile/', UploadTicketFile.as_view()),
    path('createticketchat/', CreateticketChat.as_view()),
    path('getallticketschat/', GetAllTicketsChat.as_view()),
    path('getalluserticketschat/', GetAllUserTicketsChat.as_view()),
    path('getticketdetails/', GetTicketDetails.as_view()),
    path('createcustomersurvey/', CreateCustomerSurvey.as_view()),
    path('createtechniciansurvey/', CreateTechnicianSurvey.as_view()),
    path('createcustomersurvey/', CreateCustomerSurvey.as_view()),
    path('getcustomersurveypoints/', GetCustomerSurveyPoints.as_view()),
    path('gettechniciansurveypoints/', GetTechnicianSurveyPoints.as_view()),
    path('sendticketnotification/',SendTicketNotification.as_view()),
]


