bldg_type = BuildingType.objects.all()
    if request.method == 'POST':
        bldg = Building()
        building_name = request.POST.get('building_name')
        name_of_owner = request.POST.get('name_of_owner')
        building_type_id = request.POST.get("building_type")
        building_type = BuildingType.objects.get(id = int(building_type_id))
        number_of_rooms = request.POST.get('number_of_rooms')
        mobile_number = request.POST.get('mobile_number')
        current_lease_period = request.POST.get('current_lease_period')

        bldg.building_name = building_name
        bldg.name_of_owner = name_of_owner
        bldg.building_type = building_type
        bldg.number_of_rooms = number_of_rooms
        bldg.mobile_number = mobile_number
        bldg.current_lease_period = current_lease_period

        if not building_name:
            return redirect('new_building')
        elif not name_of_owner:
            return redirect('new_building')
        elif not building_type:
            return redirect('new_building')
        elif not number_of_rooms:
            return redirect('new_building')
        elif not mobile_number:
            return redirect('new_building')
        elif not current_lease_period:
            return redirect('new_building')
        else:
            bldg.save()
            return redirect('buildings')
    else:


    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'})),
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'})),
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'})),
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'})),
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'})),