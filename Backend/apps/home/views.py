from django.shortcuts import render
from .forms import DateSelectionForm
from .models import VehicleType, Variation,Slot
from .models import Category
from django import forms 


def Home(request):
    categories = Category.objects.all()
    return render(request, 'home/home.html', {'categories': categories})

def VehicleDetails(request, id):
    vehicleType = VehicleType.objects.filter(category=id)
    return render(request, 'vehicletype.html', {'vehicletypes':vehicleType})


def Selectvariation(request,id):
    variation = Variation.objects.filter(vehicle_type=id)
    return render(request, 'variation.html', {'variations':variation})

def SelectDate(request):
    form =DateSelectionForm()
    slot_choices = [(slot.timeslot, slot.get_timeslot_display()) for slot in Slot.objects.filter(is_available=True)]
    form.fields['slot'] = forms.ChoiceField(choices=slot_choices, widget=forms.Select())

    return render(request, 'date.html',{'date':form})


