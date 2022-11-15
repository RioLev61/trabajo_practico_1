from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader
from cac.forms import ContactoForm, CategoriaForm, CategoriaFormValidado

from django.contrib import messages
from cac.models import Categoria
from django.views.generic import ListView
from django.views import View


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
    template = loader.get_template('cac/publica/quienes_somos.html')
    context = {'titulo': 'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context, request))


def blog(request):
    template = loader.get_template('cac/publica/blog.html')
    context = {'titulo': 'Blog'}
    return HttpResponse(template.render(context, request))

def contacto(request):
    #template = loader.get_template('cac/publica/contacto.html')
    #context = {'titulo': 'Contacto'}
    #return HttpResponse(template.render(context, request))
    if request.method =="POST":
        contacto_form = ContactoForm(request.POST)
    else:
        contacto_form = ContactoForm()
    return render(request,'cac/publica/contacto.html',{'contacto_form': contacto_form})





   
def index_administracion(request):
    variable = 'test_variable'
    return render(request,'cac/administracion/index_administracion.html',{'variable':variable})

def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'cac/administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaFormValidado(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado()
    return render(request,'cac/administracion/categorias/nuevo.html',{'formulario':formulario})

def categorias_editar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CategoriaFormValidado(request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado(instance=categoria)
    return render(request,'cac/administracion/categorias/editar.html',{'formulario':formulario})

def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')

class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'lista_categorias'
    template_name= 'cac/administracion/categorias/index.html'
    queryset= Categoria.objects.filter(baja=False)
    ordering = ['nombre']

class CategoriaView(View):
    form_class = CategoriaForm
    template_name = 'cac/administracion/categorias/nuevo.html'

    def get(self, request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'formulario':form})
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias_index')
        return render(request,self.template_name,{'formulario':form})



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
