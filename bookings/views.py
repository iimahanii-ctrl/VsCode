from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import BookingForm

def index(request):
    return render(request, 'bookings/index.html')

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            # Send email to Mrs. Ghorbani
            send_mail(
                subject=f'New Booking: {booking.name}',
                message=f'Name: {booking.name}\nPhone: {booking.phone}\nType: {booking.student_type}\nDay: {booking.preferred_day}\nMessage: {booking.message}',
                from_email='noreply@example.com',
                recipient_list=['mrs.ghorbani@example.com'],  # Change this
            )
            
            return redirect('success')
    else:
        form = BookingForm()
    
    return render(request, 'bookings/form.html', {'form': form})

def success(request):
    return render(request, 'bookings/success.html')