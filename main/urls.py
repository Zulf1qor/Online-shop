from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('shop/', shop_view, name='shop_url'),
    path('shop_detail/', shop_detail_view, name="shop_detail_url"),
    path('cart_view/', cart_view, name="cart_view_url"),
    path('chackout_view/', chackout_view, name="chackout_view_url"),
    path('contact_view/', contact_view, name="contact_view_url"),
    path('not_found_view/', not_found_view, name="not_found_view_url"),
    path('testimonial_view/', testimonial_view, name="testimonial_view_url"),
]