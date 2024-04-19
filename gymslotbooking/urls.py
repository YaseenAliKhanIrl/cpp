from django.urls import path
from .views import book_slot, booking_success

urlpatterns = [
    path('book/', book_slot, name='book'),
    path('success/', booking_success, name='success'),
]
