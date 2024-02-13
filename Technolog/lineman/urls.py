from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index),
    path('user/', views.AuthAPI.as_view()),
    path('report/', views.ReportCreateAPI.as_view()),
    #path('get_all_machines/', views.MachineList.as_view()),
]