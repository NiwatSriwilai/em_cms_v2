import logging
import webbrowser as wb
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
def index(request):
    #https://access.line.me/oauth2/v2.1/login?returnUri=%2Foauth2%2Fv2.1%2Fauthorize%2Fconsent%3Fscope%3Dprofile%26response_type%3Dcode%26state%3D12345abcde%26redirect_uri%3Dhttp%253A%252F%252F35.197.130.54%252Fcallback.html%26client_id%3D1594794852&loginChannelId=1594794852&loginState=9pSz0AXSXEaDkgfjaZqfxo
    #wb.open_new_tab('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://35.197.130.54/callback.html')
    return render(request, 'index.html', context=None)
    #HttpResponse("Hello, world. xxx")
    #return HttpResponse("Hello, world. You're at the polls index.")

#def about(request):
#    return render(request, 'about.html', context=None)
def callback(request):
    #print(request.GET.get('name', '')+' B = '+request.GET.get('b', ''))
    #return HttpResponse(request.GET['name'])
    #return render(request, 'index.html', context=None)
    return render(request, 'about.html', context=None)
#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'about.html', context=None)
#class AboutPageView(TemplateView):
#    template_name = "about.html"
#https://www.quora.com/How-do-I-add-my-Django-projects-on-GitHub#
#https://scotch.io/tutorials/working-with-django-templates-static-files
