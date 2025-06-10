# Fitness Booking App (Django)

A web application to view, book, and manage fitness classes like Yoga, Zumba, and HIIT. Built using Django and styled with Bootstrap.

---

## Features

- View available upcoming fitness classes
- Book a class (auto-select on click)
- Track bookings by email (API)
- Responsive UI with Bootstrap
- Admin panel to manage sessions
- Confirmation popup after booking


## Setup Instructions

### 1. Clone and enter the project
```
git clone https://github.com/alanjosetom/fitness_booking.git
cd fitness_booking
```
### 2. Set up virtual environment
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a superuser (optional, for admin)
```
python manage.py createsuperuser
```
### 6. Start the server
```
python manage.py runserver
```
## URLs
- App Home: http://localhost:8000/

- Admin: http://localhost:8000/admin/

- API: GET /bookings?email=test@example.com

 ## Optional Seed Script
 ```
python seed_classes.py
```
You can run seed_classes.py to pre-fill fitness classes
