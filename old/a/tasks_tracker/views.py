from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, TaskFilterForm
from .mixins import IsUserOwnerMixin
from core.utils import current

status_colors = {
    "todo": "#ffe100",
    "inprogress": "db0000",
    "done": "green"
}

priority_colors = {
    "low": "green",
    "medium": "#dce000",
    "high": "#f7b900",
    "critical": "red"
}


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
        context['colors'] = priority_colors
        context['current'] = current('list')

        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = priority_colors
        context['current'] = current('detail')

        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'create'
        context['current'] = current('create')

        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(IsUserOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'update'
        context['current'] = current('update')

        return context


class TaskDeleteView(IsUserOwnerMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = current('delete')

        return context
