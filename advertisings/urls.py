from django.urls import path

from .views import AdvertisingDetailView, AdvertisingListView, AdvertisingUpdateView, AdvertisingCreateView, AdvertisingDeleteView, AdvertisingSearchView


urlpatterns = [ 
  path('', AdvertisingListView.as_view(), name='advertisings'),   
  path('detalhe/<int:pk>/', AdvertisingDetailView.as_view(), name='advertising'),
  path('altera/<int:pk>/', AdvertisingUpdateView.as_view(), name='update-advertising'),
  path('cria/', AdvertisingCreateView.as_view(), name='create-advertising'),
  path('deleta/<int:pk>/', AdvertisingDeleteView.as_view(), name='delete-advertising'),
  path('pesquisa', AdvertisingSearchView, name='search'),
]
