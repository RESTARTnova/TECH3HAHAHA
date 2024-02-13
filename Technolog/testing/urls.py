from django.urls import path

from . import views

urlpatterns = [
    path('', views.testing),
    path('foreign_key/', views.GetTestingForeignKey.as_view()),
    path('foreign_key_f/', views.GetTestingForeignKeyF.as_view()),
    path('foreign_key_id_filter/', views.GetTestingForeignKeyIdFilter.as_view())
]