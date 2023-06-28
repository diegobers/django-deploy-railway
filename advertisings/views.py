from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advertising
from .choices import price_choices, state_choices


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


def AdvertisingSearchView(request):
  queryset_list = Advertising.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Price
  if 'final_price' in request.GET:
    final_price = request.GET['final_price']
    if final_price:
      queryset_list = queryset_list.filter(final_price_lte=final_price)
      
  context = {    
    'state_choices': state_choices,
    'price_choices': price_choices,
    'products': queryset_list,
    'values': request.GET
  }

  return render(request, 'advertisings/search.html', context)