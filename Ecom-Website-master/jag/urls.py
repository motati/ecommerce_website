from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jag-home'),
    path('cart/', views.cart, name='jag-cart'),
    path('orders/', views.orders, name='jag-orders'),
    path('mobile/', views.mobile, name='jag-mobile'),
    path('ordered/', views.ordered, name='jag-ordered'),
    path('laptop/', views.laptop, name='jag-laptop'),
    path('painting/', views.painting, name='jag-painting'),
    path('canvas/', views.canvas, name='jag-canvas'),
    path('clothing/', views.clothing, name='jag-clothing'),
]