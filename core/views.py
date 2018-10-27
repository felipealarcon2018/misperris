from django.shortcuts import render, redirect
from .models import Raza,Estado,Mascotas,Ciudad, Postulante, Region,Tipo_vivienda
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario_m(request):

    estado = Estado.objects.all()
    raza = Raza.objects.all()
    variables = {
        'estado': estado,
        'raza': raza
    }   
    


    if request.POST:
        mascota = Mascotas()
        mascota.nombre = request.POST.get('txtNombreMascota')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza        
        mascota.genero = request.POST.get('txtGenero')
        mascota.fecha_ingreso = request.POST.get('dtFechaIng')
        mascota.fecha_nacimiento = request.POST.get('dtFechaNac')
        mascota.descripcion = request.POST.get('txtDescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado


        
        
        try:
            mascota.save()
            variables['mensaje'] = 'Guardado Correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'




    return render(request, 'core/formulario_m.html',variables)


def formulario(request):

    tipo_vivienda = Tipo_vivienda.objects.all()
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()

    variables = {
        'tipo_vivienda':tipo_vivienda,
        'region': region,
        'ciudad': ciudad
    }

    if request.POST:
        postulante = Postulante()
        postulante.nombre = request.POST.get('txtnombre')        
        postulante.fechaNacimiento = request.POST.get('txtfecha_nac')
        postulante.telefono = request.POST.get('txttelefono')
        postulante.correo = request.POST.get('txtcorreo')
        region = Region()
        region.id = request.POST.get('cboregion')
        postulante.region = region
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cbociudad')
        postulante.ciudad = ciudad
        tipo_vivienda = Tipo_vivienda()
        tipo_vivienda.id = request.POST.get('cbotipo_vivienda')
        postulante.tipo_vivienda = tipo_vivienda

        try:
            postulante.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'
    
    return render(request, 'core/formulario.html', variables)    

#crud de mascotas

def listar_mascotas(request):

    mascota = Mascotas.objects.all()


    return render(request, 'core/listar_mascotas.html', {
        'mascota':mascota
        
    })



def eliminar_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    
    try:
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado_mascotas')


def modificar_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    estado = Estado.objects.all() 
    raza = Raza.objects.all()
    variables = {
        'mascota':mascota,
        'estado':estado,
        'raza':raza
    }


    if request.POST:
        mascota = Mascotas()
        mascota.id = request.POST.get('txtId')
        mascota.nombre = request.POST.get('txtNombreMascota')        
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza        
        mascota.genero = request.POST.get('txtGenero')
        mascota.fecha_ingreso = request.POST.get('dtFechaIng')
        mascota.fecha_nacimiento = request.POST.get('dtFechaNac')
        mascota.descripcion = request.POST.get('txtDescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado


        
        try:
            mascota.save()
            messages.success(request, 'Modificado Correctamente')
        except:
            messages.error(request, 'no se ha podido modificar')
        return redirect('listado_mascotas')


    return render(request, 'core/modificar_mascota.html', variables)



def listar_postulante(request):

    postulante = Postulante.objects.all()


    return render(request, 'core/listar_postulante.html', {
        'postulante':postulante
        
    })



def eliminar_postulante(request, id):
    postulante = Postulante.objects.get(id=id)
    
    try:
        postulante.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listar_postulante')

    
    
def modificar_postulante(request, id):
    tipo_vivienda = Tipo_vivienda.objects.all()
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()
    variables = {
        'tipo_vivienda':tipo_vivienda,
        'region': region,
        'ciudad': ciudad
    }


    if request.POST:
        postulante = Postulante()
        postulante.nombre = request.POST.get('txtnombre')        
        postulante.fechaNacimiento = request.POST.get('txtfecha_nac')
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cbociudad')
        postulante.ciudad = ciudad
        region = Region()
        region.id = request.POST.get('cboregion')
        postulante.region = region      
        postulante.telefono = request.POST.get('txttelefono')
        postulante.correo = request.POST.get('txtcorreo')        
        tipo_vivienda = Tipo_vivienda()
        tipo_vivienda.id = request.POST.get('cbotipo_vivienda')
        postulante.tipo_vivienda = tipo_vivienda


        
        try:
            postulante.save()
            messages.success(request, 'Modificado Correctamente')
        except:
            messages.error(request, 'no se ha podido modificar')
        return redirect('listar_postulante')


    return render(request, 'core/modificar_postulante.html', variables)

        
   