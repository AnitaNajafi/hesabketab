from django.shortcuts import render

def myfirstpost(request):
    return render(request, "posts/myfirstpost.html")
