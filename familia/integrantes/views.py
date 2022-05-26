from django.shortcuts import render
from integrantes.models import Familiar

# Create your views here.

def familiar (request):
    familiar_nuevo1 = Familiar.objects.create(nombre = 'Fernando', nacimiento = '1990-01-02', documento = 11222333,)
    familiar_nuevo2 = Familiar.objects.create(nombre = 'Carlos', nacimiento = '1987-03-03', documento = 22333444,)
    familiar_nuevo3 = Familiar.objects.create(nombre = 'Maria', nacimiento = '2005-04-10', documento = 33444555,)

    context = {'familar_nuevo1': familiar_nuevo1, 'familar_nuevo2': familiar_nuevo2, 'familar_nuevo3': familiar_nuevo3,}
    
    return render(request,'familiares.html', context = context)
