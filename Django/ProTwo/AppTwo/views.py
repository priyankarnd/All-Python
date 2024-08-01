from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

#Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    helpdict = {'help_insert' : "Hello, helping from views.py!"}
    return render(request,'AppTwo/help.html', context=helpdict)

def users(request):
    webpages_list = User.objects.order_by('emailid')
    email_dict = {'users':webpages_list}
    return render(request,'AppTwo/users.html',context=email_dict)