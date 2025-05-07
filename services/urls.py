from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('book/<int:service_id>/', views.create_service_checkout, name='make_booking'),
    path('booking/success/', views.booking_success, name='booking_success'),

]
