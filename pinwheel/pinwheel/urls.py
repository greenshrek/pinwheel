"""pinwheel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from speech_app import views as speech_app_views
from chat_app import views as chat_app_views
from django.conf.urls import include

urlpatterns = [
    #path('speech/', speech_app_views.index, name="index"),
    #path('chat/', chat_app_views.index, name="index"),
    url(r'^speech/', include('speech_app.urls')),
    url(r'^chat/', include('chat_app.urls')),
    url(r'^admin/', admin.site.urls),
]
