from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import BookingForm
from .models import Booking
from services.models import Service
from django.contrib.auth.decorators import login_required 
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

def book_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Store both messages in session
            request.session['booking_message'] = f"📅 Booking confirmed for {booking.service.name} on {booking.date} has been confirmed."
            request.session['payment_message'] = "🎉 Payment received successfully. Thank you for trusting PawfectMatch with your pet care needs! 🐾"

            # Stripe checkout
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
    booking_message = request.session.pop('booking_message', None)
    payment_message = request.session.pop('payment_message', None)

    return render(request, 'bookings/booking_success.html', {
        'booking_message': booking_message,
        'payment_message': payment_message,
    })

# ✅ NEW: View for displaying user's bookings
@login_required
def view_bookings(request):
    """Display the current user's bookings."""
    bookings = Booking.objects.filter(email=request.user.email)  # Use email or FK if exists
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})
