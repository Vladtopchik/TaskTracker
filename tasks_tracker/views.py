from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, TaskFilterForm
from .mixins import IsUserOwnerMixin


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)

        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskUpdateView(IsUserOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskDeleteView(IsUserOwnerMixin, DeleteView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')
