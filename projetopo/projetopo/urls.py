from django.contrib import admin
from django.urls import path
from apppo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # URL da página inicial
    path('config/', views.config, name='config'),  # URL da página config
    path('resultados/', views.resultados, name='resultados'),  # URL da página resultados
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)