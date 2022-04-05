from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Site made by me :)")
