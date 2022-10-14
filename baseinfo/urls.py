from .views import CreateDesignJson, GetAllDesignJson,GetRegins,getNabours,getApplience,getProblems,CreateProvince,\
    CreateCounty,CreateCity,CreateRegion,CreateNeighbourhood,EditProvince,EditCounty,EditCity,EditRegion,\
    EditNeighbourhood,DeleteProvince,DeleteCounty,DeleteCity,DeleteRegion,DeleteNeighbourhood,CreateAppliance,\
    CreateBrand,CreateModel,EditAppliance,EditBrand,EditModel,DeleteAppliance,DeleteBrand,DeleteModel,\
    CreateApplianceCategoryProblem,EditApplianceCategoryProblem,DeleteApplianceCategoryProblem
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

    path('createappliance/', CreateAppliance.as_view()),
    path('createbrand/', CreateBrand.as_view()),
    path('createmodel/', CreateModel.as_view()),
    path('editappliance/', EditAppliance.as_view()),
    path('editbrand/', EditBrand.as_view()),
    path('editmodel/', EditModel.as_view()),
    path('deleteappliance/', DeleteAppliance.as_view()),
    path('deletebrand/', DeleteBrand.as_view()),
    path('deletemodel/', DeleteModel.as_view()),
    path('createappliancecategoryproblem/', CreateApplianceCategoryProblem.as_view()),
    path('editappliancecategoryproblem/', EditApplianceCategoryProblem.as_view()),
    path('deleteapplianceaategoryproblem/', DeleteApplianceCategoryProblem.as_view()),

]