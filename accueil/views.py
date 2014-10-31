# from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = "accueil.html"


class UserCreateView(FormView):
    template_name = 'sign_up.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(UserCreateView, self).form_valid(form)