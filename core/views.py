from django.shortcuts import render, redirect
from .models import Persona
from .models import Gato
from .forms import PersonaForm, GatoForm
from django.contrib import messages




# Create your views here.
def home(request):
	# accedemos al objeto que contiene los datos de la base
	# el método all traerá todos los vehículos que estan en la tabla, es como el  select
	personas= Persona.objects.all()
	#ahora crearemos un diccionario donde pasaremos los datos del vehículo al template
	#ahora se agrega para enviarlo al template y se manda la variable datos que es donde queda el diccionario
	return render(request, 'home.html',context={'datos':personas})




def index(request):
    return render(request, 'index.html')

def gale(request):
    return render(request, 'gale.html')


def login(request):
    return render(request, 'login.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def mantenedor(request):
    return render(request, 'mantenedor.html')

def catalogo(request):
    gatos= Gato.objects.all()
    return render(request, 'catalogo.html',context={'datos':gatos})

def ver_gatos(request):
    gatos= Gato.objects.all()
    return render(request, 'core/ver_gatos.html',context={'gatos':gatos})
    
 
def ver_personas(request):
    personas= Persona.objects.all()
    return render(request, 'core/ver_personas.html',context={'personas':personas})


#def form_vehiculo(request):
#	return render(request,'core/form_vehiculo.html')
def form_persona(request):
    if request.method=='POST': 
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            persona_form.save()
            return redirect('home')
    else:
        persona_form= PersonaForm()
    return render(request, 'core/form_persona.html', {'persona_form': persona_form})



def form_gato(request):
    if request.method=='POST': 
        gato_form = GatoForm(request.POST)
        if gato_form.is_valid():
            gato_form.save()
            return redirect('catalogo')
    else:
        gato_form= GatoForm()
    return render(request, 'core/form_gato.html', {'gato_form': gato_form})


def form_mod_gato(request,id):
    gato = Gato.objects.get(id_chip=id)

    datos ={
        'form': GatoForm(instance=gato) 
    }
    if request.method== 'POST':
        formulario = GatoForm(data=request.POST, instance = gato)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "modificado exitosamente")
            return redirect('ver_gatos')
    return render(request, 'core/form_mod_gato.html', datos)


def form_borrar_gato(request,id):
    gato= Gato.objects.get(id_chip=id)
    gato.delete()
    messages.success(request, "eliminado exitosamente")
    return redirect('ver_gatos')
    

def form_mod_persona(request,id):
    persona = Persona.objects.get(rut=id)

    datos ={
        'form': PersonaForm(instance=persona) 
    }
    if request.method== 'POST':
        formulario = PersonaForm(data=request.POST, instance = persona)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "modificado exitosamente")
            return redirect('ver_personas')
    return render(request, 'core/form_mod_persona.html', datos)


def form_borrar_persona(request,id):
    persona= Persona.objects.get(rut=id)
    persona.delete()
    messages.success(request, "eliminado exitosamente")
    return redirect('ver_personas')
    
