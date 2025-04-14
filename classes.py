class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer({self.id}, {self.name}, {self.email})"

    def update_name(self, new_name):
        self.name = new_name

class Movie: 
    def __init__(self, id, title, genre, description, rating, picture):
        self.id = id 
        self.title = title 
        self.genre = genre 
        self.description = description
        self.rating = rating
        self.picture = picture

    def __repr__(self):
        return f"Movie({self.id}, {self.title}, {self.genre}, {self.description}, {self.rating})"
    

class Screening:
    def __init__(self, id, movie_id, datetime, hall, seats_total, seats_left):
        self.id = id
        self.movie_id = movie_id
        self.datetime = datetime  # Теперь это строка
        self.hall = hall
        self.seats_total = seats_total
        self.seats_left = seats_left

    def __repr__(self):
        return f"Screening(id={self.id}, movie_id={self.movie_id}, datetime={self.datetime}, hall={self.hall}, seats_total={self.seats_total}, seats_left={self.seats_left})"


class Booking:
    def __init__(self, id, screening_id, customer_id, seats, booked_at):
        self.id = id
        self.screening_id = screening_id
        self.customer_id = customer_id
        self.seats = seats
        self.booked_at = booked_at

    def __repr__(self):
        return f"Booking(id={self.id}, screening_id={self.screening_id}, customer_id={self.customer_id}, seats={self.seats}, booked_at={self.booked_at})"