
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.job_list)),#kol function dertlha el url ta3eha
    path('<int:id>',views.job_detail)),#f hada el path nezido haja o li hiya id lazem yerja3eli haja w li hiya integer id 
]
