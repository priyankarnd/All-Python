from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    # Check to see if we get a POST back
    if request.method == 'POST':
        # In which case we pass in that request
        form = forms.FormName(request.POST)

        # Check to see if form is valid
        if form.is_valid():
            # Do something
            print("Form validation success. Prints in console.")
            print("Name" + form.cleaned_data['name'])
            print("Email" + form.cleaned_data['email'])
            print("Text" + form.cleaned_data['text'])

    return render(request,'basicapp/form_page.html',{'form':form})

