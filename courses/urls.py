from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.CourseView.as_view(), name="course"),
    url(r'^list/$',views.CoursesView.as_view(), name="course"),
    
)
