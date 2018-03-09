from django.conf.urls import patterns, url 
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),      # /polls/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),       # /polls/5/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),     # /polls/5/results/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),      # /polls/5/vote/
)
