from django.shortcuts import redirect, render
from .models import Laboratorio

def insertar_lab(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('mostrar/')
    else:
        return render(request, 'insertar.html')

def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'mostrar.html', {'laboratorios': laboratorios})

def editar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
#así se arregló, no estaba guardando las nuevas instancias del objeto
    if request.method == 'POST':
        laboratorio.nombre = request.POST.get('nombre')
        laboratorio.ciudad = request.POST.get('ciudad')
        laboratorio.pais = request.POST.get('pais')
        laboratorio.save()
        return redirect('/laboratorio/mostrar/')

    else:
        context = {
        'laboratorio': laboratorio,
        }

    return render(request=request, template_name='editar.html', context=context)

def eliminar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/laboratorio/mostrar/')

    context = {
        'laboratorio': laboratorio,
    }

    return render(request, 'eliminar.html', context)