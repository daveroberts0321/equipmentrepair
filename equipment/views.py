from django.shortcuts import render
from .models import Clients, Equipment, Repairs

# Create your views here.

def home(request):
    # get client list from database
    clients = Clients.objects.all()
    context = {'clients': clients}   
    
    return render(request, 'home.html', context)

def equipment(request, client_id):
    # get equipment list from database
    equipment = Equipment.objects.filter(client=client_id)
    client = Clients.objects.get(id=client_id)
    context = {
      'equipment': equipment,
      'client': client,
      }
    
    return render(request, 'equipment.html', context)

def repairs(request, equipment_id):
    # get repair list from database
    repairs = Repairs.objects.filter(equipment=equipment_id)
    equipment = Equipment.objects.get(id=equipment_id)
    client = Clients.objects.get(id=equipment.client.id)
    context = {
        'repairs': repairs,
        'equipment': equipment,
        'client': client,       
        }
    
    return render(request, 'repairs.html', context)
