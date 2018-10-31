from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import ListShopView
urlpatterns = [
    path('', view = views.index, name='index'),
    path('about/', view = views.about, name='about'),
    path('register/', view = views.register, name='register'),
    path('test_template/', view = views.test_template, name='test_template'),
    path('inh_template/', view = views.inh_template, name='inh_template'),
    path('bootstrap/', view = views.bootstrap, name='bootstrap'),
    path('chat_client/', view = views.chat_client, name='chat_client'),
    path('chat_tv/', view = views.chat_tv, name='chat_tv'),
    path('vote/<int:id>/<int:p_id>', view = views.vote, name='vote'),
    path('floor', view = views.floor, name='floor'),
    path('shops/<int:pk>/', views.ShopsViewSet.as_view()),
    url(r'^shops2/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
    #path('shops/', ListShopView.as_view(), name="shops-all")
    #path('about2/', view = views.about, name='about2'),
    #path('callback/', view = views.callback, name='callback'),
    #url('', views.HomePageView.as_view()),
    #url('/about', views.AboutPageView.as_view()),
]
#python manage.py migrate
