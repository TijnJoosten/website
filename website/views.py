from django.shortcuts import render
from django.template import loader

def homePageView(request):
    return render(request, 'website/homepage.html')

def aboutPageView(request):
    return render(request, 'website/about.html')

def testPageView(request):
    return render(request, 'website/testfile.html')
