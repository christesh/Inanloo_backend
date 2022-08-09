from .views import sendsms, register, checksms, GetPersonCategories
from django.urls import path

urlpatterns = [
    path('sendsms/', sendsms.as_view()),
    path('register/', register.as_view()),
    path('checksms/', checksms.as_view()),
    path('GetPersonCategories/', GetPersonCategories.as_view()),
]