from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoptable_list, name='adoptable_list'),
    path('<int:pk>/', views.adoptable_detail, name='adoptable_detail'),
    path('add/', views.add_pet, name='add_pet'),
    path('edit/<int:pk>/', views.edit_pet, name='edit_pet'),
    path('delete/<int:pk>/', views.delete_pet, name='delete_pet'),
]
