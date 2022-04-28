from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView, name="homepage"),
    path("about", aboutPageView, name="about me"),
    path("test", testPageView, name="testpage"),
]