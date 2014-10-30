#from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "accueil.html"


class SignInView(TemplateView):
    template_name = "sign_in.html"