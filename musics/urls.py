from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playlist/', views.api_playlist),
    path('playlist/delete/<str:music_title>/<str:music_artist>/', views.api_delete),
    path('playlist/<str:music_title>/<str:music_artist>/<str:music_thumbnail>/', views.api_music),
]