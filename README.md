# Fitness Booking API

This is a simple Booking API for a fictional fitness studio (Yoga, Zumba, HIIT).

## 📦 Tech Stack

- Python 3
- Flask
- SQLite (in-memory/local DB)
- Postman / cURL for API testing

---

## 📌 Endpoints

### 1. View Classes

## GET /classes

[
    {
        "available_slots": 7,
        "datetime": "2025-06-05 07:00:00",
        "id": 1,
        "instructor": "Anita",
        "name": "Yoga"
    },
    {
        "available_slots": 8,
        "datetime": "2025-06-05 09:00:00",
        "id": 2,
        "instructor": "Ravi",
        "name": "Zumba"
    },
    {
        "available_slots": 5,
        "datetime": "2025-06-05 18:00:00",
        "id": 3,
        "instructor": "Sneha",
        "name": "HIIT"
    }
]
### 2. Book a Class

## POST /book

Body:
```json
{
  "class_id":"1",
  "client_name": "Bhavya",
  "client_email":"bhavya.mettupalli@gmail.com"
}

Response:

{
    "message":"Booking Confirmed"
}

3. View Bookings by Email

GET /bookings?email=bhavya.mettupalli@gmail.com

[
    {
        "booking_id": 1,
        "class_name": "Yoga",
        "datetime": "2025-06-05 07:00:00",
        "instructor": "Anita",
        "timestamp": "2025-06-04 14:40:55"
    }
]    
