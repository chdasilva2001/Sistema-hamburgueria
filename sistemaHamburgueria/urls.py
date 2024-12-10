from django.contrib import admin
from django.urls import path
from app1.views import Inicio,pedido,Login,Cadastro

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pedido',pedido),
    path('Login',Login),
    path('Cadastro',Cadastro),

    path('', Inicio, name='inicio') 
]
