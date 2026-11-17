import requests
from django.shortcuts import render
from django.utils import timezone

def index(request):
    today = timezone.localdate()
    hijri = None
    error = None
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH/{today.day}-{today.month}-{today.year}", timeout=10)
        response.raise_for_status()
        hijri = response.json().get("data", {}).get("hijri")
    except requests.RequestException:
        error = "تعذر تحميل التاريخ الهجري حالياً."
    return render(request, "islamic_calendar/index.html", {"today": today, "hijri": hijri, "error": error})
