from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from view.tabs.my_bookings_tab import MyBookingsTab
from view.tabs.new_booking_tab import NewBookingTab

class MainApp(QWidget):
    def __init__(self, customer):
        super().__init__()
        self.setWindowTitle("Movie Ticket Booking System")
        self.resize(600, 400)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tabs.addTab(MyBookingsTab(customer), "My Bookings")
        self.tabs.addTab(NewBookingTab(customer), "New Booking")

        layout.addWidget(self.tabs)
        self.setLayout(layout)
