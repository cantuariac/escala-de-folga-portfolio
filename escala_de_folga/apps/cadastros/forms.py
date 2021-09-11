from django.forms import ModelForm, widgets, DateField, ModelChoiceField, Form
from .models import *


class MedicoForm(ModelForm):

    class Meta:
        model = Medico
        fields = "__all__"
        widgets = {
            'admissao': widgets.DateInput(attrs={'type': 'date'})
        }
    
class PostoForm(ModelForm):
    
    class Meta:
        model = Posto
        fields = "__all__"

class FolgaForm(Form):
    data = DateField()
    medico = ModelChoiceField(queryset=Medico.objects.filter())
    


class FolgaModelForm(ModelForm):
    
    class Meta:
        model = Folga
        fields = "__all__"
        widgets = {
            'data': widgets.DateInput(attrs={'type': 'date'}),
        }

class EscalaForm(ModelForm):
    
    class Meta:
        model = Escala
        fields = "__all__"
        widgets = {
            'data': widgets.DateInput(attrs={'type': 'date'})
        }

    
