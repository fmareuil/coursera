from django.conf.urls import patterns, include, url
from django.contrib import admin
from accueil import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('accueil.urls'), name="accueil"),
    url(r'^course/$',include("courses.urls"))
)
