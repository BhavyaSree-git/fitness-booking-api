**Fitness Booking API**

A simple RESTful Booking API for a fictional fitness studio offering Yoga, Zumba, and HIIT classes.

**🎯 Objective**

Build a backend API to allow clients to:

View available fitness classes

Book spots in a class (if slots are available)

View their existing bookings by email

**📦 Tech Stack**

Python 3.x

Flask (can be replaced with Django or FastAPI)

SQLite (in-memory database for simplicity)

pytz for timezone management

unittest for basic unit tests

Logging for request and error tracking

**🛠️ Features & API Endpoints**
# 1. GET /classes

Returns a list of all upcoming fitness classes.

Each class includes:

id

name (e.g., Yoga, Zumba, HIIT)

datetime (in the requested timezone, default IST)

instructor

available_slots

Sample Response
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Yoga",
    "datetime": "2025-06-10T09:00:00+05:30",
    "instructor": "Anita Sharma",
    "available_slots": 5
  },
  {
    "id": 2,
    "name": "Zumba",
    "datetime": "2025-06-10T11:00:00+05:30",
    "instructor": "Rahul Verma",
    "available_slots": 3
  }
]
## 2. POST /book

Accepts booking requests with the following JSON body:

json
Copy
Edit
{
  "class_id": 1,
  "client_name": "Bhavya",
  "client_email": "bhavya.mettupalli@gmail.com"
}
Validates:

All fields are present and valid

The class exists

Slots are available

On success, reduces available slots by 1 and returns confirmation.

Handles overbooking errors.

Sample Success Response
json
Copy
Edit
{
  "message": "Booking confirmed for Yoga on 2025-06-10T09:00:00+05:30",
  "booking_id": 123
}
Sample Error Response (e.g., no slots left)
json
Copy
Edit
{
  "error": "No slots available for this class."
}

### 3. GET /bookings?email=<client_email>

Returns all bookings made by a specific email address.

If no bookings found, returns an empty list.

Sample Response
json
Copy
Edit
[
  {
    "booking_id": 123,
    "class_name": "Yoga",
    "datetime": "2025-06-10T09:00:00+05:30",
    "instructor": "Anita Sharma"
  }
]

**⏰ Timezone Management**

Classes are created and stored internally in IST timezone.

API supports a query parameter ?timezone=Europe/London (or any valid timezone string) on the /classes and /bookings endpoints to return date/time adjusted to the requested timezone.

Defaults to IST if no timezone specified.

Timezone handling implemented via pytz library.

**📝 Validation & Error Handling**

Input validation for required fields.

Proper HTTP status codes:

200 OK for successful GETs

201 Created for successful booking

400 Bad Request for missing/invalid data

404 Not Found for invalid class IDs

409 Conflict for overbooking attempts

Clear error messages in JSON response.


**🧪 Running the Project**

Prerequisites
Python 3.7+

pip

Setup
Clone the repo:

bash
Copy
Edit
git clone https://github.com/BhavyaSree-git/fitness-booking-api.git
cd fitness-booking-api
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
The API will be available at http://localhost:5000


**🔧 Sample cURL Requests**

Get Classes (default IST)
bash
Copy
Edit
curl http://localhost:5000/classes
Get Classes in a Different Timezone 
bash
Copy
Edit
curl "http://localhost:5000/classes?timezone=UTC"
Book a Class
bash
Copy
Edit
curl -X POST http://localhost:5000/book \
-H "Content-Type: application/json" \
-d '{"class_id":1,"client_name":"Bhavya","client_email":"bhavya.mettupalli@gmail.com"}'
Get Bookings by Email
bash
Copy
Edit
curl "http://localhost:5000/bookings?email=bhavya.mettupalli@gmail.com"

**🧪 Running Tests**

Basic unit tests for validation and booking logic included.

Run tests using:

bash
Copy
Edit
python -m unittest discover tests

**📁 Sample Seed Data**

Classes seeded on app start with:

id	name	datetime (IST)	instructor	available_slots
1	Yoga	2025-06-10 09:00:00+05:30	Anita Sharma	10
2	Zumba	2025-06-10 11:00:00+05:30	Rahul Verma	8
3	HIIT	2025-06-11 07:00:00+05:30	Meera Patel	12

**🎥 Loom Video**

Include a link to your Loom video walkthrough explaining the project, API endpoints, design decisions, and a demo.

**📞 Contact**

If you have any questions, feel free to reach out at bhavya.mettupalli@gmail.com.

Happy coding & enjoy your fitness journey! 🧘‍♂️🏋️‍♀️💪
