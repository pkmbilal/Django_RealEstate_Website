from django.shortcuts import render, redirect
from .forms import BuildingForm
from webapp.models import Building, BuildingType

# Create your views here.

def Home(request):
    return render(request, 'index.html', {'context':'null'})

def Buildings(request):
    building_list = Building.objects.all()
    return render(request, 'buildings.html', {'context': 'Buildings', 'building_list': building_list})

def Rooms(request):
    return render(request, 'rooms.html', {'context':'Rooms'})

def Customers(request):
    return render(request, 'customers.html', {'context':'Customers'})

def Receipts(request):
    return render(request, 'receipts.html', {'context':'Receipts'})

# New Building
def NewBuilding(request):
    bldg_type = BuildingType.objects.all()
    form = BuildingForm()
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buildings')    
        else:
            form = BuildingForm()
    return render(request, 'new_building.html', {'context':'NewBuilding', 'bldg_type':bldg_type, 'form':form})

# Update Building
def UpdateBuilding(request, bldg_id):
    bldg_type = BuildingType.objects.all()
    Update_building = Building.objects.get(id=bldg_id)
    form = BuildingForm(instance=Update_building)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=Update_building)
        if form.is_valid():
            form.save()
            return redirect('buildings')
    return render(request, 'update_building.html', {'context':'UpdateBuilding', 'bldg_type':bldg_type, 'form':form})

# Delete Building
def DeleteBuilding(request, bldg_id):
    building_list = Building.objects.all()
    if request.method == "POST":
        bldg=Building.objects.get(id=bldg_id)
        bldg.delete()
        return redirect('buildings')
    return render(request, 'buildings.html', {'building_list':building_list})

def NewRoom(request):
    return render(request, 'new_room.html', {'context':'NewRoom'})

def NewCustomer(request):
    return render(request, 'new_customer.html', {'context':'NewCustomer'})

def NewReceipt(request):
    return render(request, 'new_receipt.html', {'context':'NewReceipt'})

def Login(request):
    return render(request, 'login.html')

def Signup(request):
    return render(request, 'signup.html')