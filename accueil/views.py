# from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


class HomeView(TemplateView):
    template_name = "accueil.html"


class SignInView(FormView):
    template_name = "sign_in.html"
    form_class = AuthenticationForm
    success_url = '/'