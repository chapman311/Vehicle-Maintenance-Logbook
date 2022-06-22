from django.urls import path

from . import views

app_name = 'maint_log'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('get-vehicles/', views.getVehicles),
    path('add-vehicle/', views.addVehicle),
    path('delete-vehicle/<int:id>', views.deleteVehicle),
    path('get-maintenance-logs/<int:id>/', views.getMaintenanceLogs),
    path('add-maintenance-log/', views.addMaintenanceLog), 
    path('edit-maintenance-log/<int:id>', views.editMaintenanceLog),
    path('delete-maintenance-log/<int:id>', views.deleteMaintenanceLog), 
    path('user-login/', views.userLogin, name='user-login'),
    path('user-signup/', views.userSignUp, name='user-signup'),
    path('user-logout/', views.userLogout)
]