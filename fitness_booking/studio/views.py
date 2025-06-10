from django.shortcuts import render, redirect
from studio.models import FitnessClass, Booking
from django.utils.timezone import now
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fitness_class', 'client_name', 'client_email']

def class_list(request):
    classes = FitnessClass.objects.filter(datetime__gte=now()).order_by('datetime')
    return render(request, 'studio/class_list.html', {'classes': classes})

def book_class(request):
    class_id = request.GET.get('class_id')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.fitness_class.available_slots > 0:
                booking.save()
                booking.fitness_class.available_slots -= 1
                booking.fitness_class.save()
                return redirect('success')
            else:
                form.add_error(None, 'No available slots.')
    else:
        # Pre-select class if class_id passed in URL
        if class_id:
            try:
                initial_class = FitnessClass.objects.get(id=class_id)
                form = BookingForm(initial={'fitness_class': initial_class})
            except FitnessClass.DoesNotExist:
                form = BookingForm()
        else:
            form = BookingForm()
    return render(request, 'studio/book_class.html', {'form': form})

def success(request):
    return render(request, 'studio/success.html')

from django.http import JsonResponse

def get_bookings_by_email(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'error': 'Email is required'}, status=400)

    bookings = Booking.objects.filter(client_email=email).select_related('fitness_class')
    data = [
        {
            'class_name': b.fitness_class.name,
            'datetime': b.fitness_class.datetime,
            'instructor': b.fitness_class.instructor
        }
        for b in bookings
    ]
    return JsonResponse({'bookings': data})

