from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include
from config.custom_login import CustomLoginView

urlpatterns = [

    path('', include('condicaoRiscoMococaProjeto.urls')),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]