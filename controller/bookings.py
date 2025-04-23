from model.dao import MovieDAO, ScreeningDAO, BookingDAO
from datetime import datetime

md = MovieDAO()
sd = ScreeningDAO()
bd = BookingDAO()

def list_movies():
    return md.get_all_movies()

def list_screenings(movie_id):
    return sd.get_screenings_by_movie_id(movie_id)

def book_ticket(customer_id, screening_id, seats):
    screening = sd.get_screening_by_id(screening_id)
    if screening and screening.seats_left >= seats:
        bd.create_booking(
            screening_id=screening_id,
            customer_id=customer_id,
            seats=seats,
            booked_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        sd.update_seats(screening_id, screening.seats_left - seats)
        return True
    return False

from model.dao import BookingDAO, ScreeningDAO, MovieDAO
from datetime import datetime

bd = BookingDAO()
sd = ScreeningDAO()
md = MovieDAO()

def get_my_bookings(customer_id):
    result = []
    for b in bd.get_bookings_by_customer_id(customer_id):
        screening = sd.get_screening_by_id(b.screening_id)
        movie     = md.get_movie_by_id(screening.movie_id)
        result.append({
            "movie_title": movie.title,
            "picture"    : movie.picture,     
            "datetime"   : screening.datetime,
            "hall"       : screening.hall,
            "seats"      : b.seats
        })
    result.sort(key=lambda x: x["datetime"])
    return result




    