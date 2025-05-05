from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.make_booking, name='make_booking'),
    path('success/', views.booking_success, name='booking_success'),
]
