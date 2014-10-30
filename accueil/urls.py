from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.HomeView.as_view(), name="home"),
    url(r'^/signin$',views.SignInView.as_view(), name="signin"),
)
