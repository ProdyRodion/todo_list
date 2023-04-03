from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TaskForm
from list.models import Tag, Task


def index(request):
    """View function for the home page of the site."""

    return render(request, "list/task_list.html")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


def task_ready_or_not(request, pk=None):
    if request.method == "POST" and pk is not None:
        task = Task.objects.get(pk=pk)
        task.ready_or_not = not task.ready_or_not
        task.save()
    return redirect("todo_list:task-list")
