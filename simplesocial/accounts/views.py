from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
