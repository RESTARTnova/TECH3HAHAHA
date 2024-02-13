from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    
    # path("", views.index),
    path('get_shutdowns/', views.GetShutdowns.as_view()),
    path('get_class_shutdowns/', views.getClassShutdowns.as_view()),
    # path('shutdowndetail/<int:pk>/', views.ShutdownDetail.as_view()),
    path('shutdowndetail/', views.ShutdownDetail.as_view()),
    # path('test_shutdown/', views.test),
    # path('get_all_nodes/', views.NodeList.as_view()),
    # path('get_all_elements/', views.ElementList.as_view()),
    # path('get_all_details/', views.DetailsList.as_view()),
    # path('write_machine/',views.WriteMachine.as_view()),
    # path('write_node/',views.WriteNode.as_view()),
    # path('write_element/',views.WriteElement.as_view()),
    # path('write_detail/',views.WriteDetail.as_view()),
    # path('test_resp/', views.testResp.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)