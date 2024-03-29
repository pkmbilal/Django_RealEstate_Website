from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),

    # Buildings
    path('buildings', views.BuildingsView, name='buildings'),
    path('new_building', views.NewBuilding, name='new_building'),
    path('update_building/<int:bldg_id>', views.UpdateBuilding, name='update_building'),
    path('delete_building/<int:bldg_id>', views.DeleteBuilding, name='delete_building'),

    # Rooms
    path('rooms', views.RoomsView, name='rooms'),
    path('new_room', views.NewRoom, name='new_room'),
    path('update_room/<int:room_id>', views.UpdateRoom, name='update_room'),
    path('delete_room/<int:room_id>', views.DeleteRoom, name='delete_room'),

    # Customers
    path('customers', views.Customers, name='customers'),
    path('new_customer', views.NewCustomer, name='new_customer'),
    path('update_customer/<int:customer_id>',views.UpdateCustomer,name='update_customer'),
    path('delete_customer/<int:customer_id>',views.DeleteCustomer,name='delete_customer'),

    # Receipts
    path('receipts', views.Receipts, name='receipts'),
    path('new_receipt', views.NewReceipt, name='new_receipt'),
    path('update_receipt/<int:receipt_id>/',views.UpdateReceipt,name='update_receipt'),
    path('delete_receipt/<int:receipt_id>/',views.DeleteReceipt,name='delete_receipt')
]