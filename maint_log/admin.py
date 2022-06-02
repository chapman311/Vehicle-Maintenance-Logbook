from django.contrib import admin

from .models import Vehicle, MaintenanceItem

admin.site.register(Vehicle)
admin.site.register(MaintenanceItem)


