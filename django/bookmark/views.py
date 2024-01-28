from django.shortcuts import render


# Create your views here.
def bookmark_index(request):
    return render("bookmark.html")
