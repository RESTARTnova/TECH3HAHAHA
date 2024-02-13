from django.urls import path

from . import views

urlpatterns = [
    
    # path("", views.index),
    path('write_fault/',views.WriteFaults.as_view()),
    path('get_fault/',views.GetFaults.as_view()),
]
