from .models import Building, Room
from django.forms import ModelForm
from django import forms


class BuildingForm(ModelForm):
    building_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    name_of_owner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    # building_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
    number_of_rooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    mobile_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    current_lease_period = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control form-control-lg','type':'date'}))
    
    class Meta:
        model = Building
        fields = '__all__'

class RoomForm(ModelForm):
    room_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'}))
    # building_name = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control form-control-lg'}))
    # room_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control form-control-lg'}))
    # room_status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control form-control-lg'}))
    meter_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'maxlength':'16'}))
    account_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'}))

    class Meta:
        model = Room
        fields = '__all__'