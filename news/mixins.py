from django.shortcuts import redirect

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

class OwnerRequiredMixin:
    """
    Миксин для проверки, что текущий пользователь является владельцем объекта.
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied  # Вызываем исключение PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin:
    """
    Миксин для автоматического назначения текущего пользователя в качестве автора объекта.
    """

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

