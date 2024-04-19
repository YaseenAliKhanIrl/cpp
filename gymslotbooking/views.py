from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import GymSlot

def book_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})

def booking_success(request):
    return render(request, 'success.html')
