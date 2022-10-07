from .views import CreateDesignJson, GetAllDesignJson,GetRegins,getNabours,getApplience,getProblems,CreateProvince,\
    CreateCounty,CreateCity,CreateRegion,CreateNeighbourhood,EditProvince,EditCounty,EditCity,EditRegion,\
    EditNeighbourhood,DeleteProvince,DeleteCounty,DeleteCity,DeleteRegion,DeleteNeighbourhood
from django.urls import path

urlpatterns = [
    path('CreateDesignJson/', CreateDesignJson.as_view()),
    path('GetAllDesignJson/', GetAllDesignJson.as_view()),
    path('getregins/', GetRegins.as_view()),
    path('getnabours/', getNabours.as_view()),
    path('getapplience/', getApplience.as_view()),
    path('getproblems/', getProblems.as_view()),
    path('createprovince/', CreateProvince.as_view()),
    path('createcounty/', CreateCounty.as_view()),
    path('createcity/', CreateCity.as_view()),
    path('createregion/', CreateRegion.as_view()),
    path('createneighbourhood/', CreateNeighbourhood.as_view()),
    path('editprovince/', EditProvince.as_view()),
    path('editcounty/', EditCounty.as_view()),
    path('editcity/', EditCity.as_view()),
    path('editregion/', EditRegion.as_view()),
    path('editneighbourhood/', EditNeighbourhood.as_view()),
    path('deleteprovince/', DeleteProvince.as_view()),
    path('deletecounty/', DeleteCounty.as_view()),
    path('deletecity/', DeleteCity.as_view()),
    path('deleteregion/', DeleteRegion.as_view()),
    path('deleteneighbourhood/', DeleteNeighbourhood.as_view()),
]