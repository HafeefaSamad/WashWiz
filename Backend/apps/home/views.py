from django.shortcuts import render
from datetime import datetime
from datetime import date



# # Create your views here.
def Home(request):
   return render(request,'home/home.html')
