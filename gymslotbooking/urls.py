from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookslot, name='book'),
    path('success/', views.success, name='success'),
]
