from django.shortcuts import render, redirect
from .forms import BuildingForm, RoomForm, CustomerForm
from webapp.models import Building, Room, Customer
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def Home(request):
    return render(request, 'index.html', {'context':'null'})



@login_required()
def Receipts(request):
    return render(request, 'receipts.html', {'context':'Receipts'})

#------------------------Buildings------------------------------

# Show all Buildings
@login_required()
def BuildingsView(request):
    building_list = Building.objects.all()
    return render(request, 'buildings.html', {'context': 'Buildings', 'building_list': building_list})

# New Building
@login_required()
def NewBuilding(request):
    form = BuildingForm()
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buildings')    
        else:
            form = BuildingForm()
    return render(request, 'new_building.html', {'context':'NewBuilding', 'form':form})

# Update Building
@login_required()
def UpdateBuilding(request, bldg_id):
    update_building = Building.objects.get(id=bldg_id)
    form = BuildingForm(instance=update_building)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=update_building)
        if form.is_valid():
            form.save()
            return redirect('buildings')
    return render(request, 'update_building.html', {'context':'UpdateBuilding', 'form':form})

# Delete Building
@login_required()
def DeleteBuilding(request, bldg_id):
    if request.method == "POST":
        bldg=Building.objects.get(id=bldg_id)
        bldg.delete()
        return redirect('buildings')
    return redirect('buildings')

#----------------------------Rooms---------------------------------

# Show all Rooms
@login_required()
def RoomsView(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'context':'Rooms', 'rooms':rooms})

# New Room
@login_required
def NewRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('rooms')
    return render(request, 'new_room.html', {'context':'NewRoom','form':form})

# Update Room
@login_required
def UpdateRoom(request, room_id):
    update_room = Room.objects.get(id=room_id)
    form = RoomForm(instance=update_room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = update_room)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    return render(request, 'update_room.html', {'context':'UpdateRoom','form':form})

# Delete Room
@login_required
def DeleteRoom(request, room_id):
    if request.method == 'POST':
        rooms = Room.objects.get(id=room_id)
        rooms.delete()
        return redirect('rooms')
    return render(request, 'rooms.html')

@login_required()
def NewReceipt(request):
    return render(request, 'new_receipt.html', {'context':'NewReceipt'})

#----------------------------Customers---------------------------------

# Show all Customers
@login_required()
def Customers(request):
    customer_list = Customer.objects.all()
    return render(request, 'customers.html', {'context':'Customers', 'customer_list':customer_list})

# New Customer
@login_required()
def NewCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    form = CustomerForm()
    return render(request, 'new_customer.html', {'context':'NewCustomer','form':form})


# Update Customer
def UpdateCustomer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    customerForm = CustomerForm(request.POST, instance=customer)
    if request.method == 'POST':
        if customerForm.is_valid():
            customerForm.save()
            return redirect('customers')
        return render(request, 'update_customer.html',{'form':customerForm})
    else:
        customerForm = CustomerForm(instance=customer)
        return render(request, 'update_customer.html',{'context':'UpdateCustomer','form':customerForm})
    
# Delete Customer
def DeleteCustomer(request,customer_id):
    if request.method == "POST":
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return redirect('customers')
