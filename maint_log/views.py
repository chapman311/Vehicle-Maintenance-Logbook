from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

import json

from .models import Vehicle, MaintenanceItem

@login_required
def index(request):
    return render(request, 'maint_log/index.html')

def userLogin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('maint_log:index')
        else:
            context = {'message': 'Incorrect username or password.  Please try again.'}
    return render(request, 'maint_log/login.html', context)

def userSignUp(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        message = ''
        if password1 != password2:
            message += 'Passwords do not match.  '
        if User.objects.filter(username=username).exists():
            message += 'Username already taken.  '
        if not len(password1) >= 8:
            message += 'Password is too short.  '
        if password1.isnumeric():
            message += 'Password is only numbers.  '
        if password1.isalpha():
            message += 'Password is only letters.  '
        if " " in password1:
            message += 'Password contains a space.  '
        if message:
            message += 'Please try again.'
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('maint_log:index')
        context = {'message': message}
    return render(request, 'maint_log/signup.html', context)

def userLogout(request):
    logout(request)
    return redirect('/')

def getVehicles(request):
    vehicle_db = Vehicle.objects.filter(user=request.user)
    vehicles = []
    for vehicle in vehicle_db:
        vehicles.append({
            'year' : vehicle.year,
            'make' : vehicle.make,
            'model' : vehicle.model,
            'id' : vehicle.id,
            'maintenance_intervals' : vehicle.maintenance_intervals
        })
    return JsonResponse(data={'vehicles' : vehicles})

def addVehicle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        year = data.get('year')
        make = data.get('make')
        model = data.get('model')
        Vehicle.objects.create(year=year, make=make, model=model, user=request.user)
        return JsonResponse({'message': 'Vehicle Saved'})

def deleteVehicle(request,id):
    if request.method == 'POST':
        Vehicle.objects.filter(id=id).delete()
        return JsonResponse({'message': 'Vehicle Deleted'})

def getMaintenanceLogs(request, id):
    maintenance_db = MaintenanceItem.objects.filter(vehicle_id=id)
    maintenance_items = []
    for maintenance_item in maintenance_db:
        maintenance_items.append({
            'name' : maintenance_item.name,
            'date' : maintenance_item.date,
            'mileage' : maintenance_item.mileage,
            'notes' : maintenance_item.notes,
            'id' : maintenance_item.id
        })
    return JsonResponse(data={'maintenance_items': maintenance_items})

def addMaintenanceLog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        date = data.get('date')
        mileage = data.get('mileage')
        notes = data.get('notes')
        MaintenanceItem.objects.create(name=name, date=date, mileage=mileage, notes=notes, vehicle_id=data.get('vehicle'))
        return JsonResponse({'message': 'Maintenance log added.'})

def editMaintenanceLog(request, id):
    if request.method == 'POST':
        maintenance_log = MaintenanceItem.objects.get(id=id)
        data = json.loads(request.body)
        maintenance_log.name = data.get('name')
        maintenance_log.date = data.get('date')
        maintenance_log.mileage = data.get('mileage')
        maintenance_log.notes = data.get('notes')
        maintenance_log.save()
        return JsonResponse({'message': 'Maintenance log updated.'})

def deleteMaintenanceLog(request, id):
    if request.method == 'POST':
        MaintenanceItem.objects.filter(id=id).delete()
        return JsonResponse({'message': 'Maintenance log deleted.'})