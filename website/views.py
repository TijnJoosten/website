from django.shortcuts import render
from django.template import loader

def homePageView(request):
    return render(request, 'website/homepage.html')

def otherPageView(request):
    return render(request, 'website/others.html')

def testPageView(request):
    return render(request, 'website/testfile.html')
