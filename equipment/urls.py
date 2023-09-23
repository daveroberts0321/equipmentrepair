from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.home, name='home'),
    path('clientequipment/<int:client_id>/', views.equipment, name='equipment'),
    path('repairs/<int:equipment_id>/', views.repairs, name='repairs'),
]
