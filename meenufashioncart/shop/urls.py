from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='AboutUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('contact/', views.contact, name='ContactUS'),
    path('productview/', views.productView, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
    path('search/', views.search, name='Search')
]