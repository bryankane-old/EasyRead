from django.conf.urls import patterns, url
from search.views import GoogleNewsView, GradeLevelView

urlpatterns = patterns('',
    url(r'^google/$', GoogleNewsView.as_view(), name='google_news_search'),
    url(r'^level/(?P<level>\d+)$', GradeLevelView.as_view(), name='by_grade_level'),
    url(r'^level/$', GradeLevelView.as_view(), name='by_grade_level'),
)