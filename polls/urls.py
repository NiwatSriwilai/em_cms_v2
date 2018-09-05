from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', view = views.index, name='index'),
    #path('about/', view = views.about, name='about'),
    #path('about2/', view = views.about, name='about2'),
    path('callback/', view = views.callback, name='callback'),
    path('home/', view = views.home, name='home'),
    path('current_datetime/', view = views.current_datetime, name='current_datetime'),
    path('test_template/', view = views.test_template, name='test_template'),
    path('register/', view = views.register, name='register'),
    path('base/', view = views.base, name='base'),
    path('inh_template/', view = views.inh_template, name='inh_template'),
    #url('', views.HomePageView.as_view()),
    #url('/about', views.AboutPageView.as_view()),
]
#python manage.py migrate
