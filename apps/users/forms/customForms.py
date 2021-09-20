from django import forms
from ..models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField( widget=forms.PasswordInput, required = True )

    def login(self, request):
        email = self.cleaned_data.get('email') 
        password = self.cleaned_data.get('password')
        print('password: ', password)
        user = User.authenticate(email, password)
        return user

