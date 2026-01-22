from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login
import requests

import random

from .models import Action, GachaResult
from .forms import ActionForm

PRAISE_LIST = [
    "ちゃんとできててえらい！",
    "今日も生きててえらい",
    "なんだろう、君が輝いて見える",
    "橋本環奈より逸材だわ",
    "それは普通にがんばったやつ",
    "もしかして天才？",
]


@login_required
def home(request):
    today = date.today()

    today_actions = Action.objects.filter(created_at=today)
    today_result = GachaResult.objects.filter(created_at=today).first()

    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.user = request.user
            action.save()
            return redirect("gacha:home")
    else:
        form = ActionForm()

    return render(
        request,
        "gacha/home.html",
        {
            "form": form,
            "today_actions": today_actions,
            "today_result": today_result,
        },
    )

    context = {
        "form": form,
        "today_actions": today_actions,
        "today_result": today_result,
    }
    return render(request, "gacha/home.html", context)


def gacha(request):
    today = date.today()

    if not Action.objects.filter(user=request.user, created_at=today).exists():
        return redirect("gacha:home")

    result = GachaResult.objects.filter(user=request.user, created_at=today).first()
    if result is None:
        dog_img = fetch_dog_image_url()
        print("DOG IMG:", dog_img)

        result = GachaResult.objects.create(
            user=request.user,
            result_text=random.choice(PRAISE_LIST),
            image_url=dog_img,
        )

    return render(request, "gacha/result.html", {"result": result})


def history(request):
    actions = Action.objects.order_by("-created_at")
    results = GachaResult.objects.order_by("-created_at")
    return render(
        request,
        "gacha/history.html",
        {
            "actions": actions,
            "results": results,
        },
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("gacha:home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def fetch_dog_image_url():
    r = requests.get("https://dog.ceo/api/breeds/image/random", timeout=3)
    r.raise_for_status()
    data = r.json()
    url = data["message"]
    return url
