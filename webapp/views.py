from django.shortcuts import render, redirect
from .forms import BuildingForm, RoomForm, CustomerForm, ReceiptForm
from webapp.models import Building, Room, Customer, Receipt
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required()
def Home(request):
    return render(request, 'index.html')

#------------------------Buildings------------------------------

# Show all Buildings
@login_required()
def BuildingsView(request):
    if request.method == 'POST':
        searchData = request.POST.get('search')
        building_list = Building.objects.filter(Q(building_name__icontains=searchData) | Q(building_type__building_type__iexact=searchData))
        return render(request, 'buildings.html', {'context': 'Buildings', 'building_list': building_list})
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
    if request.method == 'POST':
        searchData = request.POST.get('search')
        rooms = Room.objects.filter(Q(building_name__building_name__icontains=searchData) | Q(room_number__iexact=searchData) | Q(room_status__room_status__iexact=searchData))
        return render(request, 'rooms.html', {'context': 'Rooms', 'rooms': rooms})
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

#----------------------------Customers---------------------------------

# Show all Customers
@login_required()
def Customers(request):
    if request.method == 'POST':
        searchData = request.POST.get('search')
        customer_list = Customer.objects.filter(Q(customer_name__icontains=searchData) | Q(mobile_number__iexact=searchData) | Q(id_number__iexact=searchData))
        return render(request, 'customers.html', {'context': 'Customers', 'customer_list': customer_list})
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
@login_required()
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
@login_required()
def DeleteCustomer(request,customer_id):
    if request.method == "POST":
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return redirect('customers')

#----------------------------Receipts---------------------------------

# Show all Receipts
@login_required()
def Receipts(request):
    receipt = Receipt.objects.all()
    return render(request,'receipts.html',{'context': 'Receipts', 'receipts':receipt})

# New Receipt
@login_required()
def NewReceipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipts')
    else:
        form = ReceiptForm()
        return render(request, 'new_receipt.html', {'context':'NewReceipt', 'form':form})

# Update Receipt
@login_required
def UpdateReceipt(request,receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)
    form = ReceiptForm(request.POST, instance=receipt)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('receipts')
    else:
        form = ReceiptForm(instance=receipt)
        return render(request,'update_receipt.html',{'context':'UpdateReceipt','form':form})

# Delete Receipt
@login_required
def DeleteReceipt(request,receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)
    receipt.delete()
    return redirect('receipts')