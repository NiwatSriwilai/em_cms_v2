
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
def index(request):
    return render(request, 'index.html', context=None)
    #HttpResponse("Hello, world. xxx")
    #return HttpResponse("Hello, world. You're at the polls index.")
def about(request):
    return render(request, 'about.html', context=None)
def about2(request):
    return render(request, 'about.html', context=None)
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)
class AboutPageView(TemplateView):
    template_name = "about.html"
#https://www.quora.com/How-do-I-add-my-Django-projects-on-GitHub#
#https://scotch.io/tutorials/working-with-django-templates-static-files
