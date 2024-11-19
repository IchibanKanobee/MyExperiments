from django.urls import path
from . import views

urlpatterns = [
    path('create_single_payment_checkout_session/', views.create_single_payment_checkout_session, name='create-single-payment-checkout-session'),
    path('create_subscription_checkout_session/', views.create_subscription_checkout_session, name='create-subscription-checkout-session'),
    path('single_payment_checkout/', views.single_payment_checkout, name='single-payment-checkout'),
    path('subscription_checkout/', views.subscription_checkout, name='subscription-checkout'),
    path('success/', views.success, name='checkout-success'),
    path('cancel/', views.cancel, name='checkout-cancel')
]   