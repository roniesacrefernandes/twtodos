from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Todo

#def home(request):
#    return render(request, "todos/home.html")

#def todo_list(request):
#    todos = Todo.objects.all()
#3    return render(request, "todos/todo_list.html", {"todos": todos})

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list")