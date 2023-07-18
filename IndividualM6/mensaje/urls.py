from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mensaje_bienvenida'),
    path('bienvenida/', views.mensaje_bienvenida, name='mensaje_bienvenida'),
]