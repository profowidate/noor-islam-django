import requests
from django.shortcuts import render

def index(request):
    city = request.GET.get("city", "Cairo").strip() or "Cairo"
    country = request.GET.get("country", "Egypt").strip() or "Egypt"
    timings, date, error = None, None, None
    try:
        url = "https://api.aladhan.com/v1/timingsByCity"
        response = requests.get(url, params={"city": city, "country": country, "method": 5}, timeout=12)
        response.raise_for_status()
        data = response.json().get("data", {})
        timings = data.get("timings")
        date = data.get("date", {}).get("readable")
    except (requests.RequestException, ValueError):
        error = "لم نتمكن من جلب المواقيت. تحقق من الإنترنت وحاول مجدداً."
    prayer_names = [("Fajr","الفجر"),("Sunrise","الشروق"),("Dhuhr","الظهر"),("Asr","العصر"),("Maghrib","المغرب"),("Isha","العشاء")]
    return render(request, "prayer_times/index.html", {"city": city, "country": country, "timings": timings, "date": date, "error": error, "prayer_names": prayer_names})
