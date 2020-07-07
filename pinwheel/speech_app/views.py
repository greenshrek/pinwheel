from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'first_line':"Hello this is from speech app views", 
    'second_line':"watch out the stars"}
    return render(request,'speech_app/index.html',context=my_dict)