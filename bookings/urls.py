from django.urls import path
from . import views


urlpatterns = [
    path('book/<int:service_id>/', views.book_service, name='book_service'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.view_bookings, name='view_bookings'),
]
