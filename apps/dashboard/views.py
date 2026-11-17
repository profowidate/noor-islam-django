from django.shortcuts import render
from django.utils import timezone

def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html", {"today": timezone.localdate()})
