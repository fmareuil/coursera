from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from models import Course

# Create your views here.
class CourseView(TemplateView):
    template_name = "courses.html"
    model = Course
    
    def get_context_data(self, *args, **kwargs):
        context = super(CourseView, self).get_context_data(*args, **kwargs)
        context['courses'] = Course.objects.all()
        # ajout de setting dans la conf generale
        return context
