from model.classes import Customer, Movie, Screening, Booking
import sqlite3


class CustomerDAO:
    def __init__(self, db_name = "movie_booking.db"):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)
    
    def create_customer(self, name, email, password):
        with self._connect() as conn:
            crs = conn.cursor()
            crs.execute("INSERT INTO Customers (name, email, password) VALUES (?, ?,?)", (name, email, password))
            conn.commit()
            return crs.lastrowid
        

    def get_customer_by_email(self, email):
         with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, email, password FROM Customers WHERE email = ?",
                (email,)
            )
            row = cursor.fetchone()
            if row:
                return Customer(*row)
            return None
        

    def get_all_customers(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, password FROM Customers")
            rows = cursor.fetchall()
            return [Customer(*row) for row in rows]
        
    def delete_customer(self, customer_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customers WHERE id = ?", (customer_id,))
            conn.commit()
            return cursor.rowcount
        

    def update_customer_name(self, customer_id, new_name):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Customers SET name = ? WHERE id = ?",
                (new_name, customer_id)
            )
            conn.commit()
            return cursor.rowcount
        


class MovieDAO:
    def __init__(self, db_name="movie_booking.db"):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_movie(self, title, genre, description, rating, picture=None):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Movies (title, genre, description, rating, picture) "
                "VALUES (?, ?, ?, ?, ?)",
                (title, genre, description, rating, picture)
            )
            conn.commit()
            return cursor.lastrowid

    def get_movie_by_id(self, movie_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, title, genre, description, rating, picture "
                "FROM Movies WHERE id = ?",
                (movie_id,)
            )
            row = cursor.fetchone()
            if row:
                return Movie(*row)  # Создаем объект Movie
            return None

    def get_all_movies(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, title, genre, description, rating, picture FROM Movies"
            )
            rows = cursor.fetchall()
            return [Movie(*row) for row in rows]
        
    def delete_movie(self, id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Movies where id = ?", (id,)
            )
            conn.commit()
            return cursor.rowcount

class ScreeningDAO:

    def __init__(self, dbname = "movie_booking.db"):
        self.dbname = dbname

    def _connect(self):
        return sqlite3.connect(self.dbname)
    
    def create_screening(self, movie_id, datetime, hall, seats_total, seats_left):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Screenings (movie_id, datetime, hall, seats_total, seats_left) VALUES (?, ?, ?, ?, ?)", (
                movie_id, datetime, hall, seats_total, seats_left
            ))
            conn.commit()
            return cursor.lastrowid

    def delete_screening(self, id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SCreenings where id = ?", (id,))
            conn.commit()
            return cursor.rowcount
        

    def get_screenings_by_movie_id(self, movie_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Screenings WHERE movie_id = ?", (movie_id,))
            rows = cursor.fetchall()
            return [Screening(*row) for row in rows]
        
    def get_screening_by_id(self, screening_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Screenings WHERE id = ?", (screening_id,))
            row = cursor.fetchone()
            return Screening(*row) if row else None

    def update_seats(self, screening_id, new_seats_left):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Screenings SET seats_left = ? WHERE id = ?", (new_seats_left, screening_id))
            conn.commit()

    
class BookingDAO:
    def __init__(self, dbname = "movie_booking.db"):
        self.dbname = dbname

    def _connect(self):
        return sqlite3.connect(self.dbname)
    
    def create_booking(self, screening_id, customer_id, seats, booked_at):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Bookings (screening_id, customer_id,seats,booked_at) Values (?, ?, ?, ?)", (screening_id, customer_id, seats, booked_at))
            conn.commit()
            return cursor.lastrowid
        
    def get_bookings_by_customer_id(self, customer_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Bookings WHERE customer_id = ?", (customer_id,))
            rows = cursor.fetchall()
            return [Booking(*row) for row in rows]

class CodesDAO:
    def __init__(self, dbname = "movie_booking.db"):
        self.dbname = dbname

    def _connect(self):
        return sqlite3.connect(self.dbname)
    
    def get_by_email(self, email):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT code FROM Codes where email = ?", (email,))
            code = cursor.fetchone()
            if code:
                return code[0]
            return None
    
    def create(self, email, code):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Codes (email, code) Values (?, ?)", (email, code))
            conn.commit()
            return cursor.lastrowid

    def delete(self, email):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Codes where email = ?", (email,))
            conn.commit()
            return cursor.rowcount
    





