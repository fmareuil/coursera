from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from models import Course

# Create your views here.

class CourseView(DetailView):
    template_name = "course.html"
    model = Course