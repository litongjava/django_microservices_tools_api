from django.http import HttpResponse


def index(request):
    """访问首页的视图"""
    return HttpResponse("pong")
