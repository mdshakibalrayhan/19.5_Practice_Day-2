from .models import MusicianModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'

        
class RegistraionForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']