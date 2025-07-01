from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForms
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def task_list(request):
    tasks = Tasks.objects.all()
    print('tasks :',tasks)
    return render(request,'todo/task_list.html',{'tasks':tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
            
    else:
        form = TaskForms()
        
    return render(request,'todo/create_task.html',{'form':form})

def update_task(request,pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Task updated')
            return redirect('task_list')
    else:
        form = TaskForms(instance=task)
        
    return render(request,'todo/update_task.html',{'form':form,'task':task})

def delete_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.delete()
    return redirect('task_list')

@api_view(['GET'])
def get_tasks(request):
    # print('\n')
    tasks = Tasks.objects.all()
    # print('tasks :',tasks)
    # print('\n')
    serializer = TaskSerializer(tasks, many=True)
    # print('serializer :',serializer)
    # print('\n')
    # print('serializer.data :',serializer.data)
    foo = Response(serializer.data)
    # print('\n')
    # print('Response(serializer.data) :',type(foo))
    return foo
    
@api_view(['POST'])
def add_task_api(request):
    print('request.POST :',request.data)
    form = TaskForms(request.data)
    if form.is_valid():
        form.save()
        return Response({"success":True},status = status.HTTP_201_CREATED)
    else:
        return Response({"success":False, "errors":form.errors}, status=status.HTTP_400_BAD_REQUEST)