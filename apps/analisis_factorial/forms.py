from django.forms import ModelForm
from .models import ProyectoAnalisisFactorial, Estudio


class ProyectoAnalisisFactorialForm(ModelForm):

    class Meta:
        model = ProyectoAnalisisFactorial
        fields = '__all__'


class EstudioForm(ModelForm):

    class Meta:
        model = Estudio
        fields = '__all__'
