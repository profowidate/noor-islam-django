from django.shortcuts import render

def index(request):
    return render(request, "tasbeeh/index.html")
