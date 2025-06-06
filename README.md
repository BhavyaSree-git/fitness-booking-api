# 🧘‍♀️ Fitness Booking API

This is a simple RESTful Booking API for a fictional fitness studio offering Yoga, Zumba, and HIIT classes.

---

## 📦 Tech Stack

- **Python 3**
- **Flask**
- **SQLite (in-memory/local DB)**
- **Postman** or **cURL** for API testing

---

## 📌 API Endpoints

### 1. View All Classes

**GET** `/classes`

🔍 Returns a list of all upcoming fitness classes.

#### ✅ Example Response:
```json
[
  {
    "id": 1,
    "name": "Yoga",
    "datetime": "2025-06-05 07:00:00",
    "instructor": "Anita",
    "available_slots": 7
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
2. Book a Class
POST /book

Request Body:
{
  "class_id": "1",
  "client_name": "Sree",
  "client_email": "sree@gmail.com"
}
Success Response:
{
  "message": "Booking Confirmed"
}
3. View Bookings by Email
GET /bookings?email=sree@gmail.com

Sample Response:
[
  {
    "booking_id": 1,
    "class_name": "Yoga",
    "datetime": "2025-06-05 07:00:00",
    "instructor": "Anita",
    "timestamp": "2025-06-04 14:40:55"
  }
]
Setup Instructions
# Clone the repo
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py