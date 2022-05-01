from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView, name="homepage"),
    path("work", workPageView, name="work experience"),
    path("test", testPageView, name="testpage"),
]