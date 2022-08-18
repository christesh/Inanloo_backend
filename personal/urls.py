from .views import SendSms, Register, CheckSms, GetPersonCategories, JustSms
from django.urls import path

urlpatterns = [
    path('sendsms/', SendSms.as_view()),
    path('register/', Register.as_view()),
    path('checksms/', CheckSms.as_view()),
    path('GetPersonCategories/', GetPersonCategories.as_view()),
    path('justsms/', JustSms.as_view()),
]