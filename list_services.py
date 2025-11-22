#!/usr/bin/env python
"""
Script to list all services in the database.
"""

import sqlite3

# Database file path
DB_FILE = 'consultancy.db'

def list_services():
    """List all services in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Get all services
    cursor.execute('SELECT id, name, price, duration FROM services ORDER BY price')
    services = cursor.fetchall()
    
    print("All Services in Database:")
    print("-" * 50)
    for service in services:
        print(f"ID: {service[0]}, Name: {service[1]}, Price: ₹{service[2]:,}, Duration: {service[3]} min")
    
    # Close connection
    conn.close()

if __name__ == '__main__':
    list_services()