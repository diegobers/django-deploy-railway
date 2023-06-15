from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Advertising


class AdvertisingDetailView(DetailView):
    model = Advertising
    template_name = 'advertisings/advertising.html'
    context_object_name = 'advertising'