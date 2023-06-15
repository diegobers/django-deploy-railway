from django.urls import path

from .views import AdvertisingsListView

urlpatterns = [
    path('', AdvertisingsListView.as_view(), name='index'),
    #path('about', views.about, name='about'),
]
