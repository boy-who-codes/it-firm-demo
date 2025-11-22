#!/usr/bin/env python
"""
Test script to verify user registration and booking flow.
"""

import sqlite3
from werkzeug.security import generate_password_hash

# Database file path
DB_FILE = 'consultancy.db'

def test_user_flow():
    """Test the complete user flow: registration, login, booking."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    
    # Create a test user
    email = "test@example.com"
    password = "testpassword"
    hashed_password = generate_password_hash(password)
    
    try:
        # Insert test user
        cursor = conn.execute('''
            INSERT INTO users (email, password, phone)
            VALUES (?, ?, ?)
        ''', (email, hashed_password, "1234567890"))
        
        user_id = cursor.lastrowid
        print(f"Created user with ID: {user_id}")
        
        # Create a test booking
        service_id = 1  # Business Strategy Consulting
        slot_id = 1     # First available slot
        
        # Create booking
        cursor = conn.execute('''
            INSERT INTO bookings (user_id, service_id, slot_id, status)
            VALUES (?, ?, ?, 'PENDING')
        ''', (user_id, service_id, slot_id))
        
        booking_id = cursor.lastrowid
        print(f"Created booking with ID: {booking_id}")
        
        # Get service price for payment
        service = conn.execute('SELECT price FROM services WHERE id = ?', (service_id,)).fetchone()
        
        # Create payment record
        conn.execute('''
            INSERT INTO payments (booking_id, amount, status)
            VALUES (?, ?, 'PENDING')
        ''', (booking_id, service['price']))
        
        # Mark slot as booked
        conn.execute('UPDATE time_slots SET is_booked = 1 WHERE id = ?', (slot_id,))
        
        conn.commit()
        print("Booking created successfully!")
        
        # Verify the booking
        booking = conn.execute('''
            SELECT b.*, s.name as service_name, s.price, ts.date, ts.start_time, ts.end_time
            FROM bookings b
            JOIN services s ON b.service_id = s.id
            JOIN time_slots ts ON b.slot_id = ts.id
            WHERE b.id = ?
        ''', (booking_id,)).fetchone()
        
        if booking:
            print(f"Verified booking: {booking['service_name']} on {booking['date']} at {booking['start_time']}")
            print(f"Amount: ₹{booking['price']:,}")
        else:
            print("Failed to verify booking")
            
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    test_user_flow()