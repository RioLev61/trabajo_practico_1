from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader


def index(request):
    if(request.method == 'GET'):
        titulo = 'Titulo cuando se accede por GET - modificado'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parameters_get = request.GET.get('otro')
    # return HttpResponse(f"""
    #     <h1>{titulo}</h1>
    #     <p>{parameters_get}</p>
    # """)
    listado_proyectos = [
        {
            'nombre': 'Nombre del Proyecto 1',
            'descripcion': 'Descripcion Proyecto',
            'categoria': 'Brand Identity',
            'tipo': '',
            'imagen': '/static/img/portfolio-img5.jpg',
            'website': 'https://www.google.com.ar'
        },
        {
            'nombre': 'Nombre del Proyecto 2',
            'descripcion': 'Descripcion Proyecto',
            'categoria': 'Web development',
            'tipo': '',
            'imagen': '/static/img/portfolio-img2.jpg',
            'website': 'https://www.google.com.ar'
        },
        {
            'nombre': 'Nombre del Proyecto 3',
            'descripcion': 'Descripcion Proyecto',
            'categoria': 'Mobile App',
            'tipo': '',
            'imagen': '/static/img/portfolio-img3.jpg',
            'website': 'https://www.google.com.ar'
        },
        {
            'nombre': 'Nombre del Proyecto 4',
            'descripcion': 'Descripcion Proyecto',
            'categoria': 'Logo Design',
            'tipo': '',
            'imagen': '/static/img/portfolio-img4.jpg',
            'website': 'https://www.google.com.ar'
        },
        {
            'nombre': 'Nombre del Proyecto 5',
            'descripcion': 'Descripcion Proyecto',
            'categoria': 'Social marketing',
            'tipo': '',
            'imagen': '/static/img/portfolio-img5.jpg',
            'website': 'https://www.google.com.ar'
        },
        {
            'nombre': 'Nombre del Proyecto 6',
            'descripcion': 'Descripcion Proyecto',
            'categoria': 'Flyer Design',
            'tipo': '',
            'imagen': '/static/img/portfolio-img6.jpg',
            'website': 'https://www.google.com.ar'
        }
    ]

    return render(request, 'cac/publica/index.html', {
        'titulo_nombre': titulo,
        'proyectos': listado_proyectos,
        'parametros': parameters_get,
        'hoy': datetime.now})


def quienes_somos(request):
    # return redirect('saludar_por_defecto')
    # return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('cac/publica/quienes_somos.html')
    context = {'titulo': 'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context, request))


def blog(request):
    # return redirect('saludar_por_defecto')
    # return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('cac/publica/blog.html')
    context = {'titulo': 'Blog'}
    return HttpResponse(template.render(context, request))


# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')


def saludar(request, nombre='Pepe'):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
        <p>Estoy haciendo mi primera prueba</p>
    """)


def ver_proyectos(request, anio, mes=1):
    return HttpResponse(f"""
        <h1>Proyectos del  - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)


def ver_proyectos_2022_07(request):
    return HttpResponse(f"""
        <h1>Proyectos del mes 7 del año 2022</h1>
        <p>Listado de proyectos</p>
    """)


def ver_proyectos_anio(request, anio):
    return HttpResponse(f"""
        <h1>Proyectos del  {anio}</h1>
        <p>Listado de proyectos</p>
    """)


def cursos_detalle(request, nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)


def cursos(request, nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
    """)
