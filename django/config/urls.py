"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from bookmark.views import bookmark_index


def index(request):
    return HttpResponse("hello")


def test(request):
    return HttpResponse("<h1>test</h1>")


def language(request, lang):
    return HttpResponse(f"<h1>{lang}페이지입니다.</h1>")


def number(request, num):
    return HttpResponse(f"<h1>{num}페이지입니다.</h1>")


def gugu(request, num):
    title = f"{num} 단 페이지 입니다."
    gugudan = []
    for i in range(1, 10):
        gugudan.append(f"{num} x {i} = {num *i}")
    text = "<br>".join(gugudan)
    return HttpResponse(f"<h1>{title}</h1> <p>{text}</p>")


def gugu(request, num):
    title = f"{num} 단 페이지 입니다."
    gugudan = []
    for i in range(1, 10):
        gugudan.append(f"{num} x {i} = {num *i}")
    text = "<br>".join(gugudan)
    return HttpResponse(f"<h1>{title}</h1> <p>{text}</p>")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("test/", test),
    path("lang/<str:lang>/", language),
    path("number/<int:num>/", number),
    path("gugu/<int:num>/", gugu),
    path("bookmark/", bookmark_index),
]
