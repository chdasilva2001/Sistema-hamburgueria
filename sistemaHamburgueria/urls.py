from django.contrib import admin
from django.urls import path
from app1.views import Inicio,Pedido,Login,Cadastro

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Pedido',Pedido),
    path('Login',Login, name="Login"),
    path('Cadastro',Cadastro, name="Cadastro"),
    path('', Inicio, name='inicio') 
]
