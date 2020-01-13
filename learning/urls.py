from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='learning'),
    url(r'^course/(?P<id>\d+)', views.course, name='course'),
]