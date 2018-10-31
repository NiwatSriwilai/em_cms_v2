import logging
import webbrowser as wb
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .shops_api import ShopSerialiser,CategorySerialiser,CategoryWithShopsSerialiser
import requests
import datetime
from django.template import loader
#import Base
#import models
from . import Base
from . import models
from rest_framework import generics
from .models import Shop,Category
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.routers import DefaultRouter
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialiser
class CategoryWithShopsViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryWithShopsSerialiser
class ShopsViewSet(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = Shop.objects.all().order_by('-date_joined')
    queryset = Shop.objects.all()
    serializer_class = ShopSerialiser
class ShopsViewSet2(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = Shop.objects.all().order_by('-date_joined')
    queryset = Shop.objects.all()
    serializer_class = ShopSerialiser
class ListShopView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerialiser
def index(request):
    #https://access.line.me/oauth2/v2.1/login?returnUri=%2Foauth2%2Fv2.1%2Fauthorize%2Fconsent%3Fscope%3Dprofile%26response_type%3Dcode%26state%3D12345abcde%26redirect_uri%3Dhttp%253A%252F%252F35.197.130.54%252Fcallback.html%26client_id%3D1594794852&loginChannelId=1594794852&loginState=9pSz0AXSXEaDkgfjaZqfxo
    #wb.open_new_tab('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://35.197.130.54/callback.html')
    return render(request, 'events/index.html', context=None)
    #HttpResponse("Hello, world. xxx")
    #HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponseRedirect('https://goo.gl/forms/C6nyTOgORk0Kgw6O2')
def about(request):
    #print(request.GET.get('name', '')+' B = '+request.GET.get('b', ''))
    #return HttpResponse(request.GET['name'])
    #return render(request, 'index.html', context=None)
    #https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=profile
    #http://niwat.pythonanywhere.com/polls/callback/?code=PzM1z4J3qpW9zWaNMx5e&state=12345abcde
    #wb.open('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=profile')
    return render(request, 'events/about.html', context=None)

def test_template(request):
    item_list = [1, 2, 3]

    context = {
        'name': 'Belal Khan',
        'fname': 'Azad Khan',
        'course': 'Python Django Framework',
        'address': 'Kanke, Ranchi, India',
        'item_list': item_list,
        'ordered_warranty': True,
        'company': 'Yip'
    }
    return render(request, 'events/test_template.html', context=context)
def vote(request,id,p_id):
    return render(request, 'events/about.html', context=None)
def floor(request):
    return render(request, 'events/floorM.html', context=None)
def bootstrap(request):
    for i in range(0,10):
        print('number = %d'%i)
    b1 = {'name':'Niwat',
          'description':'Sriwilai'
          }
    bs =[b1]

    boards = {
        'boards':bs,
        'username':'niwatdarap@gmail.com',
        'password':'Sreewilai_8'
    }
    return render(request, 'events/bootstrap.html', context=boards)
def chat_client(request):
    #p = models.Person(first_name = "Niwat",last_name = "Sriwilai");
    #p.save()
    p =  models.Person.objects.get(pk=1)
    p.last_name = "XXX"
    p.save()
    print("---p = "+p.last_name)
    print("---run index");
    context = {
        'someDjangoVariable':'Hello'
    }
    return render(request, 'events/chat-client.html', context=context)

def chat_tv(request):
    context = {
        'someDjangoVariable': 'Hello'
    }
    return render(request, 'events/tv.html', context=context)
    #return HttpResponseRedirect('http://localhost/chat/chat-client.html')
#http://localhost/chat/chat-client.html
def inh_template(request):
    cat = [1, 2, 3]
    pages = []
    page = {'name': 'page 1',
            'title': 'title 1',
            'url': 'www.google.com',
            }

    page2 = {'name': 'page 2',
             'title': 'title 2',
             'url': 'www.google.com',
             }
    base = Base.MyBase()
    base.name = 'Niwat SSSSSSSS'

    base.title = 'Sriwilai'
    pages.append(page)
    pages.append(page2)
    pages.append(base)
    context = {'category_n': 'I love you',
               'category': True,
               'pages': pages
               }

    return render(request, 'events/inh_template.html', context=context)
def requestCurl():
    data = {
            "grant_type": "authorization_code",
            "code":"6LxnpKjt1MfdwJFVviMu",
            "redirect_uri":"http://niwat.pythonanywhere.com/polls/callback/",
            "client_id":"1594794852",
            "client_secret":"31d3e4e088773ca7feaed23cd5ecc33e"
            }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    data2 = [
      ('grant_type', 'authorization_code'),
      ('code', 'xxx'),
      ('redirect_uri', 'xxx'),
      ('client_id', 'xxx'),
      ('client_secret', 'xxx'),
    ]

    response = requests.post('https://api.line.me/oauth2/v2.1/token', headers=headers, data=data)
    print ('response = '+response.text)
#requestCurl()    
#def about(request):
#    return render(request, 'about.html', context=None)
#
def callback(request):
    #print(request.GET.get('name', '')+' B = '+request.GET.get('b', ''))
    #return HttpResponse(request.GET['name'])
    #return render(request, 'index.html', context=None)
    #https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=profile
    #http://niwat.pythonanywhere.com/polls/callback/?code=PzM1z4J3qpW9zWaNMx5e&state=12345abcde
    #wb.open('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=profile')
    return render(request, 'about.html', context=None)
def register(request):
    return HttpResponseRedirect('https://goo.gl/forms/RHx0pQjEXAMz5Z9s1')
task_detail = ShopsViewSet2.as_view({
    'get': 'retrieve',
})
task_router = DefaultRouter()
task_router.register(r'tasks', ShopsViewSet2)
#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'about.html', context=None)
#class AboutPageView(TemplateView):
#    template_name = "about.html"

#https://www.quora.com/How-do-I-add-my-Django-projects-on-GitHub#
#https://scotch.io/tutorials/working-with-django-templates-static-files
#/.virtualenvs/niwat.pythonanywhere.com

#start server
#python manage.py runserver

#install new module to pythonanywhere solution
#https://stackoverflow.com/questions/29716462/pythonanywhere-django-import-error-for-requests-despite-it-being-listed

#webrtc
#https://medium.com/@martin.sikora/node-js-websocket-simple-chat-tutorial-2def3a841b61

#bootstrap
#https://getbootstrap.com/docs/4.0/utilities/spacing/
#debian command
#dpkg-query -l

#uwsgi --http :8080 --home /home/user@yipintsoi/Env/firstsite --chdir /home/sammy/firstsite -w firstsite.wsgi
