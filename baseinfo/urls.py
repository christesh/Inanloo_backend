from .views import CreateDesignJson, GetAllDesignJson
from django.urls import path

urlpatterns = [
    path('CreateDesignJson/', CreateDesignJson.as_view()),
    path('GetAllDesignJson/', GetAllDesignJson.as_view()),

]