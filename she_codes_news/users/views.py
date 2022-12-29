from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from news.models import NewsStory

# from django.contrib.auth.mixins import LoginRequiredMixin

# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'

# Create your views here.

# class CreateAccountView(LoginRequiredMixin, CreateView):

#     login_url = 'registration/login.html/'
#     redirect_field_name = 'redirect_to'

class CreateAccountView(CreateView):

    context_object_name = 'CustomUser'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):    
        return super().form_valid(form)

class EditAccountView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    form_class = CustomUserChangeForm
    model = CustomUser
    context_object_name = 'CustomUser'
    template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/viewAccount.html'
    context_object_name = 'profile'

    #get stories for current user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

     #user's stories published
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])

        return context