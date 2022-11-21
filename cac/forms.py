from django import forms
from django.forms import ValidationError
from .models import Categoria, Usuario, Posteo, Comentarios

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            params={'valor':value})
        #raise ValidationError('El nombre no puede contener números.')


class ContactoForm(forms.Form):

    TIPO_CONSULTA = (
        ('','-Seleccione-'),
        (1,'Proyectos'),
        (2,'Blog'),
        (3,'Contacto'),
    )

    nombre = forms.CharField(
            label='Nombre',
            required=False,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese solo texto'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            error_messages={
                    'required': 'Por favor completa el campo',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control','type':'email'})
            )
    asunto = forms.CharField(
            label='Asunto',
            max_length=100,
            widget= forms.TextInput(attrs={'class':'form-control'})
        )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme al Blog de Magnet',
        required=False,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1})
    )

    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        initial='2',
        widget=forms.Select(attrs={'class':'form-control'})
    )
    
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")

        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error('asunto', msg)


class PosteoForm(forms.Form):
    class Meta:
        model=Posteo
        fields= ['titulo','resumen', 'fecha', 'imagenpos', 'articulo']

    nombre=forms.CharField(
        label='Titulo', 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    nombre=forms.CharField(
        label='Resumen', 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    fecha=forms.DateField(
        label='Fecha Inicio', 
        widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
    )
    articulo = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    imagenpos = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )

'''
class PosteoForm(forms.Form):
    class Meta:
    model=Posteo
    fields='__all__'


class ComentariosForm(forms.Form):
    class Meta:
    model=Comentarios
    fields= ['nombre', 'fecha_inicio', 'descripcion']

    nombre=forms.CharField(
        label='Nombre', 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    fecha_inicio=forms.DateField(
        label='Fecha Inicio', 
        widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})


'''




class CategoriaForm(forms.Form):

      # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model=Categoria
        # fields='__all__'
        fields=['nombre']
        #exclude=('baja',)
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }

class CategoriaFormValidado(CategoriaForm):

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre.upper() == 'ORIGAMI':
            raise ValidationError('Codo a Codo no dicta cursos de esta temática')
        return nombre