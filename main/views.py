from django.shortcuts import render
from main.urls import *

def index_view(request):
    context = {

    }
    return render(request, 'index.html', context)



def shop_view(request):
    context = {

    }
    return render(request, 'shop.html', context)


def shop_detail_view(request):
    context = {

    }
    return render(request, 'shop-detail.html', context)


def cart_view(request):
    context = {

    }
    return render(request, 'cart.html', context)


def chackout_view(request):
    context = {

    }
    return render(request, 'chackout.html', context)

def contact_view(request):
    context = {

    }
    return render(request, 'contact.html', context)


def not_found_view(request):
    context = {

    }
    return render(request, '404.html', context)


def testimonial_view(reqeust):
    context = {

    }
    return render(reqeust, 'testimonial.html', context)