from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^note/(?P<id>.+)/','notes.views.detail'),
  url(r'^$','notes.views.index'),
  url(r'^create/', 'notes.views.create'),
  url(r'^tag/(?P<q>.+)/', 'notes.views.tag'),
)
