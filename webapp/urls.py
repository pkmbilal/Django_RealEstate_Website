from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('buildings', views.Buildings, name='buildings'),
    path('rooms', views.Rooms, name='rooms'),
    path('customers', views.Customers, name='customers'),
    path('receipts', views.Receipts, name='receipts'),
    path('new_building', views.NewBuilding, name='new_building'),
    path('update/<int:bldg_id>', views.UpdateBuilding, name='update_building'),
    path('delete_building/<int:bldg_id>', views.DeleteBuilding, name='delete_building'),
    path('new_room', views.NewRoom, name='new_room'),
    path('new_customer', views.NewCustomer, name='new_customer'),
    path('new_receipt', views.NewReceipt, name='new_receipt'),
    path('login', views.Login, name='login'),
    path('signup', views.Signup, name='signup'),
]