from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy


class IsAuthorisedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('task-list'))
        return super().dispatch(request, *args, **kwargs)


class IsUserOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.creator != self.request.user:
            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)
