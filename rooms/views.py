from django.shortcuts import render
from . import models

# from datetime import datetime
# from django.http import HttpResponse


def all_rooms(request):  # request를 받았으면 HttpRespense로 응답하는 구조
    all_rooms = models.Room.objects.all()
    return render(
        request,
        "rooms/home.html",
        context={"rooms": all_rooms},
    )
