from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    return render(request, "basicapp/index.html")

def form_view(request):
    form = forms.FormName;

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('name: {}'.format(form.cleaned_data.get('name')))
            print('name: {}'.format(form.cleaned_data.get('email')))
            print('name: {}'.format(form.cleaned_data.get('text')))
    return render(request, "basicapp/form_page.html", {'form':form})
