from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^admin/', include(admin.site.urls)),
)
