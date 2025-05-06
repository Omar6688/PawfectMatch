from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoptable_list, name='adoptable_list'),
    path('<int:pk>/', views.adoptable_detail, name='adoptable_detail'),
]
