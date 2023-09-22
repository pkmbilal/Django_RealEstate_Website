from .models import Building, Room, Customer, Receipt
from django.forms import ModelForm
from django import forms


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = '__all__'
        widgets = {
            'building_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'name_of_owner': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'number_of_rooms': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'current_lease_period': forms.DateInput(attrs={'class':'form-control form-control-lg','type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['building_type'].empty_label = "Select an option"
        self.fields['building_type'].widget.attrs.update({'class':'form-control form-control-lg'})

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_number': forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
            'meter_number': forms.TextInput(attrs={'class':'form-control form-control-lg', 'maxlength':'16'}),
            'account_number': forms.NumberInput(attrs={'class':'form-control form-control-lg'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['building_name'].empty_label = "Select an option"
        self.fields['building_name'].widget.attrs.update({'class':'form-control form-control-lg'})

        self.fields['room_type'].empty_label = "Select an option"
        self.fields['room_type'].widget.attrs.update({'class':'form-control form-control-lg'})

        self.fields['room_status'].empty_label = "Select an option"
        self.fields['room_status'].widget.attrs.update({'class':'form-control form-control-lg'})

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'mobile_number': forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
            'id_number': forms.TextInput(attrs={'class':'form-control form-control-lg'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_type'].empty_label = "Select an option"
        self.fields['id_type'].widget.attrs.update({'class':'form-control form-control-lg'})

        self.fields['building_name'].empty_label = "Select an option"
        self.fields['building_name'].widget.attrs.update({'class':'form-control form-control-lg'})

        self.fields['room_number'].empty_label = "Select an option"
        self.fields['room_number'].widget.attrs.update({'class':'form-control form-control-lg'})

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control form-control-lg','type':'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'start_date': forms.DateInput(attrs={'class':'form-control form-control-lg','type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control form-control-lg','type':'date'}),
            'comment': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].empty_label = "Select an option"
        self.fields['customer_name'].widget.attrs.update({'class':'form-control form-control-lg'})

        self.fields['room_number'].empty_label = "Select an option"
        self.fields['room_number'].widget.attrs.update({'class':'form-control form-control-lg'})