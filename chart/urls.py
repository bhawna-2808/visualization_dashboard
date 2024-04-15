from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from .views import *


urlpatterns = [
   path("", dashboard, name="dashboard"),
   path("api/insightdata/", InsightAPIView.as_view()),
   path("filter/", filterinsightdata, name="filterinsightdata"),
   path("data-filter/", datafilterinsightdata, name="data-filter")
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
