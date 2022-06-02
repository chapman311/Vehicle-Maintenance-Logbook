from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
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
    vehicle_db = Vehicle.objects.all()
    vehicles = []
    for vehicle in vehicle_db:
        vehicles.append({
            'year' : vehicle.year,
            'make' : vehicle.make,
            'model' : vehicle.model,
        })
    return JsonResponse(data={'vehicles' : vehicles})

def addVehicle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        year = data.get('year')
        make = data.get('make')
        model = data.get('model')
        Vehicle.objects.create(year=year, make=make, model=model)
        return JsonResponse({'message': 'Vehicle Saved'})

def getMaintenanceLogs(request):
    maintenance_db = MaintenanceItem.objects.all()
    maintenance_items = []
    for maintenance_item in maintenance_db:
        maintenance_items.append({
            'name' : maintenance_item.name,
            'date' : maintenance_item.date,
            'mileage' : maintenance_item.mileage,
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
        return JsonResponse({'message': 'Maintenance log added.'})