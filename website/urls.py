from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView, name="homepage"),
    path("others", otherPageView, name="otherpage"),
    path("test", testPageView, name="testpage"),
]