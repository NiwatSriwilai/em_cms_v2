"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.conf.urls import url
from django.urls import include, path
#from django.conf.urls import include
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#from events.shops_api import ShopViewSet

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'notes', ShopViewSet)
from events import views
router = routers.DefaultRouter()
router.register(r'shops', views.ShopsViewSet)
router.register(r'categorys', views.CategoryViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    path('polls/', include('polls.urls')),
    path('events/', include('events.urls')),
    #path('polls', include('polls.urls')),
    #path(r'^', include('polls.urls')),
    path('admin/', admin.site.urls),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/', include(router.urls)),
    #http://127.0.0.1:8000/polls/templates/index.html
    #https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://35.197.130.54/callback.html
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
