from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html', {'context':'null'})

def Buildings(request):
    return render(request, 'buildings.html', {'context':'Buildings'})

def Rooms(request):
    return render(request, 'rooms.html', {'context':'Rooms'})

def Customers(request):
    return render(request, 'customers.html', {'context':'Customers'})

def Receipts(request):
    return render(request, 'receipts.html', {'context':'Receipts'})

def NewBuilding(request):
    return render(request, 'new_building.html', {'context':'NewBuilding'})

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