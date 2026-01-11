from django.urls import path
from . import views

app_name = 'condicaoRiscoMococaProjeto'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
