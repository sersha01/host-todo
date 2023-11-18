from django.shortcuts import redirect, render

from .forms import TODOForm
from .models import TODO

# Create your views here.

def list_todo(request):
    context = {
        "tasks": TODO.objects.filter(deleted=False)
    }
    return render(request, 'list_todo.html', context)

def add_todo(request):
    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_todo')
    else:
        form = TODOForm()
    return render(request, 'add_todo.html', {'form': form})

def update_todo(request, pk):
    task = TODO.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('list_todo')

def delete_todo(request, pk):
    task = TODO.objects.get(id=pk)
    task.deleted = True
    task.save()
    return redirect('list_todo')