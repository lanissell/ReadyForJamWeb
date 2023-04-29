from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from login.forms import UserLoginForm


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = '/user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('jamList')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
