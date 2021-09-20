from django import forms
from django.forms import widgets

from ..models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ['name', 'email' , 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': "Nombres Completos"}),
            'password' : forms.PasswordInput()
        }
        
        labels = {
            'name' : "Nombres",
            'lastname' : "Apellidos",
            'email': "E-mail",
            "password" : "Contraseña"

        }

    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        #verificar que el usuario no existe
        email = cleaned_data.get("email")
        user_exists = User.user_exists(email) 
        if user_exists:
            print("Usuario Existente") 
            raise forms.ValidationError("Usuario Existente")  

        
