from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^/post/(?P<post_id>[0-9]+)$', views.edit_post, name='edit_post'),
    url(r'^/post$', views.add_post, name='add_post')
]
