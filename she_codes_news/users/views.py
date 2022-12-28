from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class CreateAccountView(CreateView):
    context_object_name = 'CustomUser'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        return super().form_valid(form)

class EditAccountView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    context_object_name = 'CustomUser'
    template_name = 'users/createAccount.html'
