from django.urls import path

from .views import AdvertisingDetailView


urlpatterns = [    
  path('detalhe/<int:pk>/', AdvertisingDetailView.as_view(), name='advertising'),
]
