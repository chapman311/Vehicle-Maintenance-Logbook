from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-maintenance-logs/', views.getMaintenanceLogs),
    path('add-maintenance-log/', views.addMaintenanceLog),
]