from django.shortcuts import render
from django.template import loader

def homePageView(request):
    template = loader.get_template('home.html')
    return render(request, 'home.html')
