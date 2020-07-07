from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'ques':"Ques: Where are you?", 
    'ans':"Ans: In this universe"}
    return render(request,'chat_app/index.html',context=my_dict)
