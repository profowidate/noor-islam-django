from django.urls import path
from . import views
urlpatterns = [path("", views.index, name="quran"), path("<int:number>/", views.read_surah, name="read_surah")]
