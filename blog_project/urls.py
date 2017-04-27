from django.conf.urls import url

from . import views

app_name = 'blog_project'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)$', views.DeleteView.as_view(), name='detail'),
    url(r'^post$', views.add_post, name='add_post')
]
