from django.urls import path
from . import views

urlpatterns = [
    path('volunteer/', views.volunteer_signup, name='volunteer_signup'),
    path('volunteer/thank-you/', views.volunteer_thank_you, name='volunteer_thank_you'),
    path('donate/', views.donate, name='donate'),
    path('donate/thank-you/', views.donation_thank_you, name='donation_thank_you'),
    path('share/', views.share, name='share'),
]
