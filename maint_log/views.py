from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

import json

from .models import Vehicle, MaintenanceItem

def index(request):
    return render(request, 'maint_log/index.html')

@login_required
def getMaintenanceLogs(request):
    maintenance_db = MaintenanceItem.objects.all()
    maintenance_items = []
    for maintenance_item in maintenance_db:
        maintenance_items.append({
            'name': maintenance_item.name,
            'date': maintenance_item.date,
            'mileage': maintenance_item.mileage,
            'notes' : maintenance_item.notes,
        })
    return JsonResponse(data={'maintenance_items': maintenance_items})

def addMaintenanceLog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        date = data.get('date')
        mileage = data.get('mileage')
        notes = data.get('notes')
        MaintenanceItem.objects.create(name=name, date=date, mileage=mileage, notes=notes)
        return JsonResponse({'message': 'ok'})
    return JsonResponse({'message': 'post requests only'})