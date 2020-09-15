from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    """ HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    # model에 뭘 넣느냐에 따라 room_detail의 값이 달라짐
    model = models.Room
