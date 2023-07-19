from django.shortcuts import render
from django.http import HttpResponse
from .forms import NuevoForm

usuarios = [
    {
        'nombre': "usuario1",
        'edad': "10",
        'mail':"usuario1@individual.m6"
    },
    {
        'nombre': "usuario2",
        'edad': "20",
        'mail':"usuario2@individual.m6"
    },
    {
        'nombre': "usuario3",
        'edad': "30",
        'mail':"usuario3@individual.m6"
    },
    {
        'nombre': "usuario4",
        'edad': "40",
        'mail':"usuario4@individual.m6"
    },
    {
        'nombre': "usuario5",
        'edad': "50",
        'mail':"usuario5@individual.m6"
    }

]
def mensaje_bienvenida(request):
    return HttpResponse("<h1> Bienvenidos a TeLoVendo </h1>")

def home(request):
    contexto ={
        'usuarios': usuarios
    }
    return render(request,'mensaje/index.html', contexto)

def crearFormulario(request):
    form = NuevoForm()
    return render(request,"mensaje/formulario.html",{'form':form})