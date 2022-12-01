from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='inicio'),
    path('quienessomos/',views.quienes_somos,name='quienes_somos'),
    path('blog/',views.blog,name='blog'),
    path('contacto/',views.contacto,name='contacto'),


    path('administracion/',views.index_administracion,name='inicio_administracion'),
    path('administracion/categorias', views.CategoriaListView.as_view(),name='categorias_index'),
    path('administracion/categorias/nuevo', views.CategoriaView.as_view(),name='categorias_nuevo'),
    path('administracion/categorias/editar/<int:id_categoria>', views.categorias_editar,name='categorias_editar'),
    path('administracion/categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),

    path('administracion/posteos', views.posteos_index,name='posteos_index'),
    path('administracion/posteos/nuevo/', views.posteos_nuevo,name='posteos_nuevo'),
    path('administracion/posteos/editar/<int:id_posteos>', views.posteos_editar,name='posteos_editar'),
    path('administracion/posteos/eliminar/<int:id_posteos>', views.posteos_eliminar,name='posteos_eliminar'),

    path('administracion/usuarios', views.usuarios_index,name='usuarios_index'),
    path('administracion/usuarios/nuevo/', views.usuarios_nuevo,name='usuarios_nuevo'),
    path('administracion/usuarios/editar/<int:id_usuarios>', views.usuarios_editar,name='usuarios_editar'),
    path('administracion/usuarios/eliminar/<int:id_usuarios>', views.usuarios_eliminar,name='usuarios_eliminar'),

    
    path('cuentas/registrarse', views.usuarios_index, name='registrarse'),

    path('account/login/',auth_views.LoginView.as_view(template_name='cac/publica/login.html')),
    # path('account/logout/',
    #      auth_views.LogoutView.as_view(template_name='cac/publica/logout.html'), name='logout'),
    path('account/password_change/',auth_views.PasswordChangeView.as_view(success_url='/')),
    path('account/',include('django.contrib.auth.urls')),


    path('hola_mundo',views.hola_mundo),
    path('saludarbonito/',views.saludar,name="saludar_por_defecto"),
    path('saludar/<str:nombre>',views.saludar,name="saludar"),
   # path('proyectos/2022/07',views.ver_proyectos_2022_07),
    #re_path(r'^proyectos/(?P<anio>\d{2,4})/$',views.ver_proyectos),
    #path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos"),
    #path('cursos/detalle/<slug:nombre_curso>',views.cursos_detalle, name="curso_detalle"),
    #re_path(r'^cursos/(?P<nombre>\w+)/$',views.cursos,name="cursos")

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)