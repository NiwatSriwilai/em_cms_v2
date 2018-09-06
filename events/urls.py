from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', view = views.index, name='index'),
    path('about/', view = views.about, name='about'),
    path('register/', view = views.register, name='register'),
    #path('about2/', view = views.about, name='about2'),
    #path('callback/', view = views.callback, name='callback'),
    #url('', views.HomePageView.as_view()),
    #url('/about', views.AboutPageView.as_view()),
]
#python manage.py migrate
