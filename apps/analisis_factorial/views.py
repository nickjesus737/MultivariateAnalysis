from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ProyectoAnalisisFactorialForm, EstudioForm
from .services import AnalisisFactorialServicio

def create_proyecto(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProyectoAnalisisFactorialForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/analisis-factorial/create-estudio/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProyectoAnalisisFactorialForm()

    return render(request, 'create_proyecto.html', {'form': form})


def create_estudio(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EstudioForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EstudioForm()

    return render(request, 'create_estudio.html', {'form': form})


def ejecutar_estudio(request, *args, **kwargs):

    if request.method == 'GET':
        estudio_id = kwargs.get('id')
        resultado = AnalisisFactorialServicio().ejecutar(estudio_id)
        return render(request, 'resultados.html', {'resultado': resultado})

