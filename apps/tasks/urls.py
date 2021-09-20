from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('task', views.task),
    path('<int:task_id>', views.task_detail),
    path('colaborate', views.colaborate),
    path('join/<int:task_id>', views.join, name ='join')
]