from django.urls import path
from . import views

urlpatterns = [
    path('', views.band_list, name='band_list'),
    path('<int:pk>/', views.band_detail, name='band_detail'),
    path('create/', views.band_create, name='band_create'),
    path('<int:pk>/update/', views.band_update, name='band_update'),
    path('<int:pk>/delete/', views.band_delete, name='band_delete'),
]
