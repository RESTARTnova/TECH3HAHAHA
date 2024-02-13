from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index),
    path('get_all_machines/', views.MachineList.as_view()),
    path('get_all_nodes/', views.NodeList.as_view()),
    path('get_all_elements/', views.ElementList.as_view()),
    path('get_all_details/', views.DetailsList.as_view()),
    path('write_machine/',views.WriteMachine.as_view()),
    path('write_node/',views.WriteNode.as_view()),
    path('write_element/',views.WriteElement.as_view()),
    path('write_detail/',views.WriteDetail.as_view()),
    path('test_resp/', views.testResp.as_view()),
]
