from .forms.task import TaskForm
from django.shortcuts import render, redirect

from .models import Task

from ..users.models import User


def home(request):
    try:
        user = User.objects.get(id = int(request.session["logged_userid"]))
        context = { 'user': user }
        if user:
            return render(request, 'home.html', context)
        else:
            return redirect('/')    
    except:
        return redirect('/') 


def task(request):
   if request.method == "POST":
       #crear el task
       # 1. obtener el objeto usuarios
       user = User.objects.get(id = int(request.session["logged_userid"]))
       task_name = request.POST['name']
       task_duedate = request.POST['due_date'] 
       #2. Creacion de Nueva Tasl
       new_task = Task.objects.create(name = task_name, due_date= task_duedate ,
                                    user= user )
       print("Nueva Tarea: ", new_task)
       return redirect('home') 

def task_detail(request, task_id):
    task = Task.objects.get(id = task_id)     
    if request.method == 'GET':
        print(task)
        taskForm = TaskForm(instance = task)
        return render(request, 'task_detail.html', {'taskForm': taskForm})
    else:
        taskForm = TaskForm(request.POST, instance=task)
        if "cancel" in request.POST:
            return redirect('home')
        if taskForm.is_valid():
            completed =  request.POST.get('completed', '') == 'on'
            task.name = request.POST['name']
            task.completed = completed
            task.save()
            return redirect('home')


def colaborate(request):
    user = User.objects.get(id = int(request.session['logged_userid']))
    all_tasks = Task.objects.all().filter(completed = False).exclude(user__id__in=[user.id])
    print('all_tasks ', all_tasks)
    context = {'all_tasks': all_tasks, 'user': user}
    return render(request, 'colaborate.html', context)


def join(request, task_id):
    task = Task.objects.get(id = task_id)
    helper = User.objects.get(id = int(request.session['logged_userid'])) 
    task.helpers.add(helper)
    task.save()
    print('helpers: ', task.helpers.all())
    return redirect('home')   




