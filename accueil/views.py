# from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


class HomeView(TemplateView):
    template_name = "accueil.html"


class LoginView(FormView):
    template_name = "sign_in.html"
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        """
        The user has provided valid credentials (this was checked in
        AuthenticationForm.is_valid()). So now we can log him in.
        """
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
