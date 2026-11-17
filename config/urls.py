from django.contrib import admin
from django.urls import path, include
from apps.dashboard.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("quran/", include("apps.quran.urls")),
    path("prayer-times/", include("apps.prayer_times.urls")),
    path("azkar/", include("apps.azkar.urls")),
    path("tasbeeh/", include("apps.tasbeeh.urls")),
    path("zakat/", include("apps.zakat.urls")),
    path("duas/", include("apps.duas.urls")),
    path("hadith/", include("apps.hadith.urls")),
    path("calendar/", include("apps.islamic_calendar.urls")),
    path("names-of-allah/", include("apps.names_of_allah.urls")),
]
