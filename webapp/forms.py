from .models import Building
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