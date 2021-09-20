
from django import forms
from django.forms import widgets
from ..models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'due_date', 'completed']
        widgets = {
            'completed' : forms.CheckboxInput(),
            'due_date' : forms.TextInput(attrs={'readonly':'readonly'})

        }
        labels ={
            'name': 'Nombre',
            'due_date' : 'Fecha Limite',
            'completed' : 'Completado'
        }
