from django.urls import path, include

from .views import LoginAuthView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('entrar/login/', LoginAuthView.as_view(), name='login'),
    path('entrar/logout/', LogoutView.as_view(next_page='base'), name='sair'),

    #path("", views.IndexView.as_view(), name="index"),

]