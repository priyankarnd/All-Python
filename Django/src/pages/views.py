from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>") # HTML code string
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact page</h1>") # HTML code string
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About page</h1>") # HTML code string
    my_context = {
        "my_text": "This is about us",
        "my_number" : 123,
        "my_list" : [10, 20, 30]
    }
    return render(request, "about.html", my_context)



