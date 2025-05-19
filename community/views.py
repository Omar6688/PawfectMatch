from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json


from .forms import VolunteerForm

stripe.api_key = settings.STRIPE_SECRET_KEY


# --- Volunteer Views ---
def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_thank_you')
    else:
        form = VolunteerForm()
    return render(request, 'community/volunteer.html', {'form': form})


def volunteer_thank_you(request):
    return render(request, 'community/volunteer_thank_you.html')


# --- Donate Views (with Stripe) ---
def donate(request):
    return render(request, 'community/donate.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data.get('amount', 1000)  

            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': amount,
                        'product_data': {
                            'name': f'PawfectMatch Donation (${amount / 100:.2f})',
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/support/donate/thank-you/'),
                cancel_url=request.build_absolute_uri('/support/donate/'),
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def donation_thank_you(request):
    return render(request, 'community/donation_thank_you.html')


# --- Share View ---
def share(request):
    return render(request, 'community/share.html')
