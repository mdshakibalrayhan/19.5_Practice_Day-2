from django.contrib.auth.forms import AuthenticationForm
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import MusicianModel
from .forms import MusicianForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .forms import RegistraionForm

@method_decorator(login_required, name='dispatch')
class AddMusicianview(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('homepage')    

def log_out_page(request):
    return render(request,'logout.html')


class EditMusicianView(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class RegistraionView(CreateView):
    model = User
    form_class = RegistraionForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
