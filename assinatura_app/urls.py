from django.urls import path
from . import views

urlpatterns = [
    path('', views.captura_assinatura, name='captura_assinatura'),
    path('sucesso/', views.sucesso, name='sucesso'),
]