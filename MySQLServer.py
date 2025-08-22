#!/usr/bin/python3
"""
Script to create database alx_book_store in MySQL server
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (change user & password if needed)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()
