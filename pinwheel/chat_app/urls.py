from django.conf.urls import url
from django.urls import path
from chat_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]