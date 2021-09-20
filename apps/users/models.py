from django.contrib.auth.hashers import check_password, make_password
from django.db import models

import re

from django.urls.resolvers import CheckURLMixin

class UserManager(models.Manager):
    def basic_validator(self, postData):
        print('basic_validator', postData)
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = 'El nombre debe tener mas de 2 caracteres'
        if len(postData['lastname']) < 2:
            errors['lastname'] = 'El Apellido debe tener mas de 2 caracteres'
        if len(postData['email']) < 2:
            print('email', postData['email'])
            errors['email'] = 'El Correo Electronico debe tener mas de 2 caracteres'
        if len(postData['email']) > 0:
            error = self.checkEmail(postData['email'])
            if len(error) > 0:
                errors['email'] = self.checkEmail(postData['email'])
        return errors 
    
    def checkEmail(self, data):
        error = ''
        print('checkEmail')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data):  
            error = "Correo Invalido"    
        return error 


class User(models.Model):
    name = models.CharField(max_length=45, blank=False, null =False)
    lastname =models.CharField(max_length=45, blank=False, null =False)
    email =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def authenticate(email, password):
        results = User.objects.filter(email = email)
        if len(results) == 1:
           #verificar que el password ingresado sea igual al guardado en BD
           user = results[0]
           saved_password = user.password     #hash
           if check_password(password, saved_password):
               print('user: ', user.name)
               return user
           return None 

    @staticmethod
    def user_exists(email):
        return User.objects.filter(email = email).exists()


