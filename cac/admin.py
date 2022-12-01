from django.contrib import admin
from cac.models import Posteo, Usuario,Categoria
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

class CacAdminSite(admin.AdminSite):
    site_header = 'Adminsitración CAC'
    site_title = 'Mi admin personalizado'
    index_title = 'Administración principal'
    empty_value_display = 'No hay datos para visualizar'


class PosteoAdmin(admin.ModelAdmin):

    #modificar listado relaciones oneToMany
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'categoria':
            kwargs['queryset'] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','baja')
    list_filter = ('baja',)

mi_admin = CacAdminSite(name='cacadmin')
mi_admin.register(Posteo,PosteoAdmin)
#admin.register(Posteo)
#admin.register(Usuario)
mi_admin.register(Categoria, CategoriaAdmin)
mi_admin.register(User,UserAdmin)
mi_admin.register(Group,GroupAdmin)