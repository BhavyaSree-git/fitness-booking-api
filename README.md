# Fitness Booking API

A simple RESTful Booking API for a fictional fitness studio offering Yoga, Zumba, and HIIT classes.

<div align="right">

[Watch the Screeccast Here](<https://github.com/BhavyaSree-git/fitness-booking-api/blob/6d5bbf93a7892e918ae9ce4a1f98b2ce0311b4ed/Omnify_Assignment_Demo.mp4>)

</div>

## 🎯 Objective

Build a backend API to allow clients to:

View available fitness classes

Book spots in a class (if slots are available)

View their existing bookings by email

### 📦 Tech Stack

Python 3.x

Flask (can be replaced with Django or FastAPI)

SQLite (in-memory database for simplicity)

pytz for timezone management

unittest for basic unit tests

Logging for request and error tracking

## 📁 Project Structure

    fitness_booking_api/
    ├── pycache/
    ├── app.py
    ├── models.py
    ├── utils.py
    ├── requirements.txt
    ├── README.md
    ├── venv/
    ├── instance/
    │ └── database.db
    └── uploads/
    ├── get_classes.png
    ├── post_book.png
    └── get_bookings.png

## 🛠️ Features & API Endpoints

**1. GET /classes**

Purpose: Get all available fitness classes.

<div style="display:flex;">
    <img src="https://github.com/BhavyaSree-git/fitness-booking-api/blob/f44732945f1e58016e0f173f95a6d095d9569b63/media/uploads/classes_get_api.png" alt="Screenshot" width="49%">
</div> 
 
Request:

Method: GET

URL: http://localhost:5000/classes

Optional query param: tz (default is Asia/Kolkata)

Sample Response
json

[
{
"id": 1,
"name": "Yoga",
"datetime": "2025-06-05 07:00:00",
"instructor": "Anita",
"available_slots": 10
},
{
"id": 2,
"name": "Zumba",
"datetime": "2025-06-05 09:00:00",
"instructor": "Ravi",
"available_slots": 8
},
{
"id": 3,
"name": "HIIT",
"datetime": "2025-06-05 18:00:00",
"instructor": "Sneha",
"available_slots": 5
}
]

**2. POST /book**

Purpose: Book a slot in a class.

<div style="display:flex;">
    <img src="https://github.com/BhavyaSree-git/fitness-booking-api/blob/f44732945f1e58016e0f173f95a6d095d9569b63/media/uploads/book_post.png" alt="Screenshot" width="49%">
</div>

Request:

Method: POST

URL: http://localhost:5000/book

Body (raw JSON):

json

{
"class_id": 1,
"client_name": "Bhavya",
"client_email": "bhavya.mettupalli@gmail.com"
}

Success Response (200):
{
"message": "Booking confirmed"
}

Error Response (Missing field):

{
"error": "Missing required fields"
}

Error Response (No slots):

{
"error": "No slots available"
}

Error Response (Class not found):
{
"error": "Class not found"
}

**3. GET /bookings?email=<client_email>**

Purpose: Get all bookings for a given email.

<div style="display:flex;">
    <img src="https://github.com/BhavyaSree-git/fitness-booking-api/blob/f44732945f1e58016e0f173f95a6d095d9569b63/media/uploads/bookings_get_api.png" alt="Screenshot" width="49%">
</div>

Request:

Method: GET

URL (with email query param):
http://localhost:5000/bookings?email=bhavya.mettupalli@gmail.com

Sample Response
json
[
{
"booking_id": 1,
"class_name": "Yoga",
"instructor": "Anita",
"datetime": "2025-06-05 07:00:00",
"timestamp": "2025-06-05 12:34:56"
}
]

Error Response (missing email):

{
"error": "Email query param is required"
}

## ⏰ Timezone Management

Classes are created and stored internally in IST timezone.

API supports a query parameter ?timezone=Europe/London (or any valid timezone string) on the /classes and /bookings endpoints to return date/time adjusted to the requested timezone.

Defaults to IST if no timezone specified.

Timezone handling implemented via pytz library.

## 📝 Validation & Error Handling

Input validation for required fields.

Proper HTTP status codes:

200 OK for successful GETs

201 Created for successful booking

400 Bad Request for missing/invalid data

404 Not Found for invalid class IDs

409 Conflict for overbooking attempts

Clear error messages in JSON response.

## 🧪 Running the Project

Prerequisites
Python 3.7+

pip

Setup
Clone the repo:
git clone https://github.com/BhavyaSree-git/fitness-booking-api.git
cd fitness-booking-api
Install dependencies:
pip install -r requirements.txt
Run the app:
python app.py
The API will be available at http://localhost:5000

## 🔧 Sample cURL Requests

Get Classes (default IST)
curl http://localhost:5000/classes
Get Classes in a Different Timezone
curl "http://localhost:5000/classes?timezone=UTC"
Book a Class
curl -X POST http://localhost:5000/book
-H "Content-Type: application/json"
-d '{"class_id":1,"client_name":"Bhavya","client_email":"bhavya.mettupalli@gmail.com"}'
Get Bookings by Email
curl "http://localhost:5000/bookings?email=bhavya.mettupalli@gmail.com"

## 🧪 Running Tests

Basic unit tests for validation and booking logic included.

Run tests using:

python -m unittest discover tests

## 📁 Sample Seed Data

Classes seeded on app start with:

id name datetime (IST) instructor available_slots
1 Yoga 2025-06-10 09:00:00+05:30 Anita Sharma 10
2 Zumba 2025-06-10 11:00:00+05:30 Rahul Verma 8
3 HIIT 2025-06-11 07:00:00+05:30 Meera Patel 12

## 🎥 Loom Video

Include a link to your Loom video walkthrough explaining the project, API endpoints, design decisions, and a demo.

## 📞 Contact

If you have any questions, feel free to reach out at bhavya.mettupalli@gmail.com.

Happy coding & enjoy your fitness journey! 🧘‍♂️🏋️‍♀️💪
