from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Advertising


class AdvertisingDetailView(DetailView):
    model = Advertising
    template_name = 'advertisings/advertising.html'
    context_object_name = 'advertising'

class AdvertisingListView(LoginRequiredMixin, ListView):
    model = Advertising
    template_name = 'advertisings/advertisings.html'
    context_object_name = 'advertisings'

class AdvertisingUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertising
    template_name = 'advertisings/create.html'
    context_object_name = 'advertising'
    fields = '__all__'
    success_url = reverse_lazy('advertisings')

class AdvertisingCreateView(LoginRequiredMixin, CreateView):
    model = Advertising
    template_name = 'advertisings/create.html'
    context_object_name = 'advertising'
    fields = ['photo_main', 'description']
    success_url = reverse_lazy('advertisings')


class AdvertisingDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertising
    template_name = 'advertisings/delete.html'
    context_object_name = 'advertising'
    success_url = reverse_lazy('advertisings')