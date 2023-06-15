from django.urls import path, include

from .views import LoginAuthView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('', LoginAuthView.as_view(), name='login'),
    path('sair/', LogoutView.as_view(next_page='index'), name='logout'),
]