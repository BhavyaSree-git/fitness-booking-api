from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, FitnessClass, Booking
from utils import convert_ist_to_timezone
from datetime import datetime
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

logging.basicConfig(level=logging.INFO)

with app.app_context():
    db.create_all()
    if not FitnessClass.query.first():
        sample_classes = [
            FitnessClass(name="Yoga", datetime_ist=datetime(2025, 6, 5, 7, 0), instructor="Anita", available_slots=10),
            FitnessClass(name="Zumba", datetime_ist=datetime(2025, 6, 5, 9, 0), instructor="Ravi", available_slots=8),
            FitnessClass(name="HIIT", datetime_ist=datetime(2025, 6, 5, 18, 0), instructor="Sneha", available_slots=5),
        ]
        db.session.bulk_save_objects(sample_classes)
        db.session.commit()


def seed_classes():
    sample_classes = [
        FitnessClass(name="Yoga", datetime_ist=datetime(2025, 6, 5, 7, 0), instructor="Anita", available_slots=10),
        FitnessClass(name="Zumba", datetime_ist=datetime(2025, 6, 5, 9, 0), instructor="Ravi", available_slots=8),
        FitnessClass(name="HIIT", datetime_ist=datetime(2025, 6, 5, 18, 0), instructor="Sneha", available_slots=5),
    ]
    db.session.bulk_save_objects(sample_classes)
    db.session.commit()

@app.route('/classes', methods=['GET'])
def get_classes():
    tz = request.args.get('tz', 'Asia/Kolkata')
    classes = FitnessClass.query.all()
    result = []
    for cls in classes:
        converted = convert_ist_to_timezone(cls.datetime_ist, tz)
        if converted is None:
            return jsonify({'error': 'Invalid timezone'}), 400
        result.append({
            'id': cls.id,
            'name': cls.name,
            'datetime': converted.strftime('%Y-%m-%d %H:%M:%S'),
            'instructor': cls.instructor,
            'available_slots': cls.available_slots
        })
    return jsonify(result), 200

@app.route('/book', methods=['POST'])
def book_class():
    data = request.get_json()
    class_id = data.get('class_id')
    name = data.get('client_name')
    email = data.get('client_email')

    if not all([class_id, name, email]):
        return jsonify({'error': 'Missing required fields'}), 400

    cls = FitnessClass.query.filter_by(id=class_id).first()
    if not cls:
        return jsonify({'error': 'Class not found'}), 404

    if cls.available_slots <= 0:
        return jsonify({'error': 'No slots available'}), 400

    booking = Booking(class_id=class_id, client_name=name, client_email=email)
    cls.available_slots -= 1
    db.session.add(booking)
    db.session.commit()

    logging.info(f"Booking confirmed for {name} in class {cls.name}")
    return jsonify({'message': 'Booking confirmed'}), 200

@app.route('/bookings', methods=['GET'])
def get_bookings():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email query param is required'}), 400

    bookings = Booking.query.filter_by(client_email=email).all()
    result = []
    for b in bookings:
        cls = FitnessClass.query.get(b.class_id)
        result.append({
            'booking_id': b.id,
            'class_name': cls.name,
            'instructor': cls.instructor,
            'datetime': cls.datetime_ist.strftime('%Y-%m-%d %H:%M:%S'),
            'timestamp': b.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
