from django.shortcuts import render, redirect
from peliculas.models import *
from django.contrib import messages

# Create your views here.

def pag_principal(request):
    return render(request, "principal.html")

def pag_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "peliculas.html",{
        'peliculas': peliculas
    })


def guardar(request):
    titulo = request.POST["titulo"]
    director = request.POST["director"]
    anio = request.POST["anio"]
    Protagonista = request.POST["Protagonista"]
    pelicula = Pelicula(
            titulo=titulo,
            director=director,
            anio=anio,
            Protagonista=Protagonista,
        )
    pelicula.save()
    messages.success(request, 'Pelicula guardada correctamente.')
    return redirect('menu_peliculas')

def eliminar(request, id):
    pelicula = Pelicula.objects.filter(pk=id)
    pelicula.delete()
    messages.success(request, 'Pelicula eliminada correctamente.')
    return redirect('menu_peliculas')

def detalle(request, id):
    pelicula = Pelicula.objects.get(pk=id)
    return render(request, "peliculaEditar.html",{
        'pelicula': pelicula
    })

def editar(request):
    titulo = request.POST["titulo"]
    director = request.POST["director"]
    anio = request.POST["anio"]
    Protagonista = request.POST["Protagonista"]
    id = request.POST["id"]
    Pelicula.objects.filter(pk=id).update(id=id, titulo=titulo, director=director, anio=anio, Protagonista=Protagonista)
    messages.success(request, 'Pelicula actualizada correctamente.')
    return redirect('menu_peliculas')