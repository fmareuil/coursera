from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, FormView
from forms import InscriptionForm
from models import Course, Language, Category, Session
from django.http import Http404
# Create your views here.


class CourseView(DetailView):
    template_name = "course.html"
    model = Course


class InscriptionView(FormView):
    form_class = InscriptionForm
    success_url = "/"

    def get_success_url(self):
        self.success_url = self.request.POST['next']
        return FormView.get_success_url(self)

    def form_valid(self, form):
        session = Session.objects.get(pk=self.request.POST['session_id'])
        session.user.add(self.request.user)
        session.save()
        return super(InscriptionView, self).form_valid(form)

    def form_invalid(self, form):
        print form
        raise Http404("Error 404")


class CoursesView(ListView):
    template_name = "courses.html"
    #model = Course
    queryset = [Course, Language, Category]

    def get_context_data(self, *args, **kwargs):
        context = super(CoursesView, self).get_context_data(*args, **kwargs)
        context['courses'] = Course.objects.all()
        context['languages'] = Language.objects.all()
        context['lang_len'] = len(Language.objects.all())
        context['categories'] = Category.objects.all()
        context['cat_len'] = len(Category.objects.all())
        # ajout de setting dans la conf generale
        #recipient_slug = self.kwargs['slug']
        #try:
        #    course = Course.objects.get(slug=recipient_slug)
        #except Course.DoesNotExist:
        #    raise Http404("no user matching slug '%s'" % recipient_slug)
        return context

