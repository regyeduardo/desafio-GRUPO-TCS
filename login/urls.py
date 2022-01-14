from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.log_out, name='logout'),
]