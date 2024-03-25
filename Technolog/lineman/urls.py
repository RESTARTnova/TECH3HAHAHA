from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index),
    path('users', views.AuthAPI.as_view()),
    path('users_job',views.JobTitlesAPI.as_view()),
    path('actions', views.ActionAPI.as_view()),
    path('rooms', views.RoomsAPI.as_view()),
    path('kys/room',views.RoomsReportAPI.as_view()),
    path('kys/action',views.ActionsReportAPI.as_view()),
    path('durability', views.DurabilityAPI.as_view()),
    path('nfc', views.NFCAPI.as_view()),
    path('log',views.LogsAPI.as_view()),
    path('reports/room',views.ReportsRoomAPI.as_view()),
    path('repots/filter/room',views.ReportsRoomFilterAPI.as_view()),
]