from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'core.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^(?P<slug>[\w-]+)/inscription$',
                           login_required(views.InscriptionView.as_view()),
                           name="inscription"),
                       url(r'^(?P<slug>[\w-]+)/$', views.CourseView.as_view(),
                           name="course"),
                       url(r'^$', views.CoursesView.as_view(), name="courses"),
                       )
