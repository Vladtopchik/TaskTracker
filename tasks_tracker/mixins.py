from django.core.exceptions import PermissionDenied


class IsUserOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        print(self.__class__)
        instance = self.get_object()

        if instance.creator != self.request.user:
            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)
