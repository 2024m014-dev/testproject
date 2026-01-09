from django.urls import path
from django.contrib import admin
from . import views

app_name = "gacha"

urlpatterns = [
    path("", views.home, name="home"),
    path("gacha/", views.gacha, name="gacha"),
    path("admin/", admin.site.urls),
    path("history/", views.history, name="history"),
    path("signup/", views.signup, name="signup"),
]
