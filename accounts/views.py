from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from core.mixins import IsAuthorisedMixin
from core.utils import current


class UserRegisterView(IsAuthorisedMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = current('login')
        context['auth'] = self.request.user.is_authenticated

        return context


class UserLoginView(IsAuthorisedMixin, LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = current('register')
        context['auth'] = self.request.user.is_authenticated

        return context

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)

        super().form_valid(form)
        return redirect(self.success_url)


@login_required
def logout_page(request):
    logout(request)
    return redirect('/')
