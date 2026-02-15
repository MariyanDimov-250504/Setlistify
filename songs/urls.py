from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:pk>/', views.song_detail, name='song_detail'),
    path('create/', views.song_create, name='song_create'),
    path('<int:pk>/update/', views.song_update, name='song_update'),
    path('<int:pk>/delete/', views.song_delete, name='song_delete'),
]
