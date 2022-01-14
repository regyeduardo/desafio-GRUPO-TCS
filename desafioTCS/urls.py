from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', include('login.urls', namespace='login')),
    path('', include('login.urls', namespace='login')),
    path('dashboard/', include('gerenciamento.urls', namespace='dashboard')),
    path('admin/', admin.site.urls),
]
