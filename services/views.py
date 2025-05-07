import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Service

stripe.api_key = settings.STRIPE_SECRET_KEY

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def create_service_checkout(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(service.price * 100),  # Convert to cents
                'product_data': {
                    'name': service.name,
                    'description': service.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/services/booking/success/'),
        cancel_url=request.build_absolute_uri('/services/'),
    )

    return redirect(session.url)

def booking_success(request):

    return render(request, 'services/booking_success.html')

