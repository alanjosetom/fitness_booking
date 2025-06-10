import os
import django
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_booking.settings')
django.setup()

from studio.models import FitnessClass

# Clear existing
FitnessClass.objects.all().delete()

# Create sample classes
classes = [
    ("Yoga", datetime(2025, 6, 11, 8, 0), "Asha", 10),
    ("Zumba", datetime(2025, 6, 12, 9, 30), "Ravi", 15),
    ("HIIT", datetime(2025, 6, 13, 7, 30), "Neha", 8),
]

for name, dt, instructor, slots in classes:
    FitnessClass.objects.create(
        name=name,
        datetime=make_aware(dt),
        instructor=instructor,
        available_slots=slots
    )

print("Sample classes seeded.")
