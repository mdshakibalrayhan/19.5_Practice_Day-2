from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .form import Albumform
from .models import AlbumModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = AlbumModel
    form_class = Albumform
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)


def home(request):
    data = AlbumModel.objects.all()

    return render(request,'home.html',{'data':data})


class EditAlbumView(UpdateView):
    model = AlbumModel
    form_class = Albumform
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class DeleteAlbumview(DeleteView):
    model = AlbumModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('homepage')