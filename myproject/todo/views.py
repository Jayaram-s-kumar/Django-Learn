from django.shortcuts import render
from .models import Tasks

# Create your views here.
def task_list(request):
    tasks = Tasks.objects.all()
    return render(request,'todo/task_list.html',{'tasks':tasks})