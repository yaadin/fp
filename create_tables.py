import sqlite3

conn = sqlite3.connect("movie_booking.db")

with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)


    conn.execute("""
    CREATE TABLE IF NOT EXISTS Movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        description TEXT NOT NULL,
        rating TEXT NOT NULL,
        picture TEXT NOT NULL
    )
    """)


    conn.execute("""
    CREATE TABLE IF NOT EXISTS Screenings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER NOT NULL,
        datetime TEXT NOT NULL,
        hall TEXT NOT NULL,
        seats_total INTEGER NOT NULL,
        seats_left INTEGER NOT NULL,
        FOREIGN KEY (movie_id) REFERENCES Movies(id)
    )
    """)


    conn.execute("""
    CREATE TABLE IF NOT EXISTS Bookings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        screening_id INTEGER NOT NULL,
        customer_id INTEGER NOT NULL,
        seats INTEGER NOT NULL,
        booked_at TEXT NOT NULL,
        FOREIGN KEY (screening_id) REFERENCES Screenings(id),
        FOREIGN KEY (customer_id) REFERENCES Customers(id)
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS Codes(
        email TEXT,
        code INTEGER
    )
    """)
   
print("created.")