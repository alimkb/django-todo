from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Todo
from .forms import TodoForm

@staff_member_required(login_url='admin:login')
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    return render(request, 'todo_app/todo_list.html', {'todos': todos, 'form': form})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
    return redirect('todo_list')

@login_required
def toggle_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('todo_list')