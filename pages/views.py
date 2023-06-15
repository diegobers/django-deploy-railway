from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from advertisings.models import Advertising


class AdvertisingsListView(ListView):
    model = Advertising
    template_name = 'pages/index.html'
    context_object_name = 'advertisings'