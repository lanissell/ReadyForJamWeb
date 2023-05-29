from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.core.cache import cache
from django.urls import reverse_lazy

from login.forms import UserLoginForm
from registration.models import UserPhoto


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = '/user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        cache.set('user_avatar', UserPhoto.objects.get(user=self.request.user).avatar, None)
        return reverse_lazy('jamList')

    def form_invalid(self, form):
        messages.error(self.request, 'Не правильный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))


class UserLogout(LogoutView):

    def get_success_url(self):
        cache.delete('user_avatar')
        return super().get_success_url()