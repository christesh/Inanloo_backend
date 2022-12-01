"""inanloo_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
DOCS_TITLE = "Inanloo Services API"
DOCS_DESCRIPTION = " "
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('order/', include('order.urls')),
    path('baseinfo/', include('baseinfo.urls')),
    path('personal/', include('personal.urls')),
    path('order/', include('order.urls')),
    path('schema/', get_schema_view(DOCS_TITLE, DOCS_DESCRIPTION)),
    path('docs/', include_docs_urls(DOCS_TITLE, DOCS_DESCRIPTION)),
    path('swagger-docs/', get_swagger_view(DOCS_TITLE)),
    path('admins/doc/', include('django.contrib.admindocs.urls')),

]
