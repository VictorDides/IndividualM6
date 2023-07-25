from django.urls import path
from . import views
from users import views as vistas_usuario
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.home, name='mensaje_bienvenida'),
    path('bienvenida/', views.mensaje_bienvenida, name='mensaje_bienvenida'),
    path('formulario/', views.crearFormulario, name='formulario'),
    path('registro/', vistas_usuario.registro, name='registro'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout' ),
    path('perfil/', vistas_usuario.perfil, name='perfil'),
]