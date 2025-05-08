from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from .forms import BookingForm
from .models import Booking
from services.models import Service
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def book_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # ✅ Store ONE clean message in session
            request.session['booking_success_message'] = (
                f"✅ Booking for {booking.service.name} on {booking.date} confirmed. "
                "💳 Payment received successfully. Thank you!"
            )

            # Stripe Checkout session
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(service.price * 100),
                        'product_data': {
                            'name': service.name,
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/bookings/success/'),
                cancel_url=request.build_absolute_uri(f'/bookings/book/{service_id}/'),
            )

            return redirect(session.url)
    else:
        form = BookingForm(initial={'service': service})

    return render(request, 'bookings/booking_form.html', {'form': form})


def booking_success(request):
    # ✅ Show and clear one clean message from session
    message = request.session.pop('booking_success_message', None)
    return render(request, 'bookings/booking_success.html', {
        'booking_success_message': message
    })
