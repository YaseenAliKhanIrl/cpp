from django.shortcuts import render, redirect
# from .forms import BookingForm
from .models import Booking

def bookslot(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        registrationdate = request.POST.get('date')
        registrationtime = request.POST.get('time')
        slotBook = Booking(
            name=username,
            email=useremail,
            date=registrationdate,
            time=registrationtime
        )
        slotBook.save()
        return redirect('success')
        
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')
