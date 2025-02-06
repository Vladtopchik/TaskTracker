from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, TaskFilterForm, CommentForm
from core.mixins import IsUserOwnerMixin
from core.utils import current, star

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
        context['auth'] = self.request.user.is_authenticated

        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()

            return redirect('task-detail', pk=comment.task.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = priority_colors
        context['current'] = current('detail')
        context['comment_form'] = CommentForm()
        context['star'] = star
        context['auth'] = self.request.user.is_authenticated

        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'create'
        context['current'] = current('create')
        context['auth'] = self.request.user.is_authenticated

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
        context['auth'] = self.request.user.is_authenticated

        return context


class TaskDeleteView(IsUserOwnerMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = current('delete')
        context['auth'] = self.request.user.is_authenticated

        return context
