from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('galaxy/', views.galaxy, name='galaxy'),
    path('upload', views.upload, name='upload'),
]