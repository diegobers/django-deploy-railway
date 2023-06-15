from django.urls import path

from .views import AdvertisingDetailView, AdvertisingListView, AdvertisingUpdateView, AdvertisingCreateView


urlpatterns = [ 
  path('', AdvertisingListView.as_view(), name='advertisings'),   
  path('detalhe/<int:pk>/', AdvertisingDetailView.as_view(), name='advertising'),
  path('altera/<int:pk>/', AdvertisingUpdateView.as_view(), name='update-advertising'),
  path('cria/', AdvertisingCreateView.as_view(), name='create-advertising'),
]
