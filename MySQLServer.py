#!/usr/bin/python3
"""
Script to create a database 'alx_book_store' in MySQL server.
If the database already exists, it won’t fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (update with your username & password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # put your root password here if you have one
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")   # Optional debug line

if __name__ == "__main__":
    create_database()
