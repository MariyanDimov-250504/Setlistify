from django.urls import path
from . import views

urlpatterns = [
    path('', views.concert_list, name='concert_list'),
    path('<int:pk>/', views.concert_detail, name='concert_detail'),
    path('create/', views.concert_create, name='concert_create'),
    path('<int:pk>/update/', views.concert_update, name='concert_update'),
    path('<int:pk>/delete/', views.concert_delete, name='concert_delete'),
    path('<int:concert_pk>/add-song/', views.add_setlist_entry, name='add_setlist_entry'),
    path('<int:concert_pk>/edit-song/<int:entry_pk>/', views.edit_setlist_entry, name='edit_setlist_entry'),
    path('<int:concert_pk>/delete-song/<int:entry_pk>/', views.delete_setlist_entry, name='delete_setlist_entry'),
]
