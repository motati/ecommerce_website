from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Canvas, Clothing, Laptop, Mobile, Painting


# login not required for home

def home(request):
    return render(request, 'jag/home.html')


# login required for home


@login_required
def ordered(request):
    return render(request, 'jag/order_success.html')


# login required for home

@login_required
def cart(request):
    return render(request, 'jag/cart.html')

@login_required
def orders(request):
    return render(request, 'jag/orders.html')


def mobile(request):
    context={
        'mobiles': Mobile.objects.all()
    }
    return render(request, 'jag/mobile.html', context)


def laptop(request):
    context={
        'laptops': Laptop.objects.all()
    }
    return render(request, 'jag/laptop.html', context)


def painting(request):
    context={
        'paintings': Painting.objects.all()
    }
    return render(request, 'jag/painting.html', context)


def canvas(request):
    context={
        'canvass': Canvas.objects.all()
    }
    return render(request, 'jag/canvas.html', context)


def clothing(request):
    context={
        'clothings': Clothing.objects.all()
    }
    return render(request, 'jag/clothing.html', context)



