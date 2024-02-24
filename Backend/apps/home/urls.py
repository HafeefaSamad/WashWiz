from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('vehicletype/<int:id>/', views.VehicleDetails, name='vehicletype'),
    path('variation/<int:id>/', views.Selectvariation, name='variation'),
    path('date/', views.SelectDate, name='date'),


]

