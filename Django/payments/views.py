import sys
sys.path.append("..")


from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from pyfin_utils.security import decrypt
import json

# Create your views here.

with open('/etc/marketsdataintelligence/config.json') as config_file:
    config = json.load(config_file)

ENCRYPT_FILE_1 = config['ENCRYPT_FILE_5']
ENCRYPT_FILE_2 = config['ENCRYPT_FILE_6']

lines = decrypt.decrypt_json(ENCRYPT_FILE_1, ENCRYPT_FILE_2)

stripe.api_key = lines["STRIPE_PRIVATE_KEY"]


@csrf_exempt
def create_single_payment_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
              'card',
            ],
            line_items=[
                {
                    # TODO: replace this with the `price` of the product you want to sell
                    'price': 'price_1JKZPUE2MQoFZWFafvqcbo4Y',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('checkout-success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('checkout-cancel')),
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)
    



@csrf_exempt
def create_subscription_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
              'card',
            ],
            line_items=[
                {
                    # TODO: replace this with the `price` of the product you want to sell
                    'price': 'price_1JK64ME2MQoFZWFaBPShUmhq',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=request.build_absolute_uri(reverse('checkout-success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('checkout-cancel')),
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)

 

def single_payment_checkout(request):
    return render(request, 'payments/single_payment_checkout.html')



def subscription_checkout(request):
    return render(request, 'payments/subscription_checkout.html')


def success(request):
    return render(request, 'payments/success.html')


def cancel(request):
    return render(request, 'payments/cancel.html')
