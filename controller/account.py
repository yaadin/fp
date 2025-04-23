from model.dao import CustomerDAO, ScreeningDAO, BookingDAO, MovieDAO, CodesDAO
from model.classes import Customer, Screening, Booking, Movie
from utils.email_utils import send_email_code
import random



cd = CustomerDAO()
waiting = CodesDAO()

def register(name, email, password):
    if cd.get_customer_by_email(email = email):
        return False
    code = str(random.randint(1000,9999))
    waiting.create(email, code)
    send_email_code(email, code)
    return [name, email, password]

def confirm(name, password, email, newcode):
    x = waiting.get_by_email(email)
    print(x)
    if not x:
        return False
    
    if newcode == x:
        cd.create_customer(name=name, email=email, password=password)
        waiting.delete(email)
        return True
    else:
        return False
    
def login(email, password):
    user = cd.get_customer_by_email(email)
    if user and user.password == password:
        return user
    else:
        return None
    
    

