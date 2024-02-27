from django.shortcuts import render,redirect
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

# def SelectDate(request):
#     form =DateSelectionForm()
#     if form.is_valid():
#         date = form.cleaned_data.get('date')

#     return render(request, 'date.html', {'date': form})

def SelectDate(request):
    if request.method == 'POST':
        form = DateSelectionForm(request.POST)
        print('ho')
        if form.is_valid():
            print(form)
            print(form.cleaned_data.get('date'),'kk ')
            date = form.cleaned_data.get('date' ,)
            for timeslot_choice in Slot.TIMESLOT_CHOICES:
                Slot.objects.create(date=date )
            return redirect('home')
    else:
        form = DateSelectionForm()
    
    return render(request, 'date.html', {'date': form})
