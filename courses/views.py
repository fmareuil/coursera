from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from models import Course

# Create your views here.

class CourseView(TemplateView):
    template_name = "courses.html"
    model = Course
    

    