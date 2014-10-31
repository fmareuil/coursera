from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^account/signin$', 'django.contrib.auth.views.login',
        {'template_name': 'sign_in.html'}, name="login"),
    url(r'^account/logout$', 'django.contrib.auth.views.logout',
        {'next_page': 'home'},
    name="logout"),
)
