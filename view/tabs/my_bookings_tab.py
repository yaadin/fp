from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget,
    QPushButton, QListWidgetItem, QLabel, QMessageBox, QDialog
)
from PyQt6.QtGui  import QPixmap
from PyQt6.QtCore import Qt
from utils.qr_utils import hall_to_link, make_qr_pixmap
from controller.bookings import get_my_bookings  


class MyBookingsTab(QWidget):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer

        self.layout = QVBoxLayout(self)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.reload_data)
        self.layout.addWidget(refresh_btn)

        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.show_qr)
        self.layout.addWidget(self.list_widget)
        self.reload_data()         


    def reload_data(self):
        self.list_widget.clear()
        self.bookings = get_my_bookings(self.customer.id)
        for b in self.bookings:
            card = QWidget()
            vbox = QVBoxLayout(card)
            vbox.setContentsMargins(0, 0, 0, 0)


            pix = QPixmap(b["picture"])
            poster_lbl = QLabel()
            poster_lbl.setPixmap(pix.scaledToWidth(120))
            vbox.addWidget(poster_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)


            caption = QLabel(
                f"{b['movie_title']}\n"
                f"Hall: {b['hall']}\n"
                f"{b['datetime']}"
            )
            caption.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            vbox.addWidget(caption)

   
            item = QListWidgetItem()
            item.setSizeHint(card.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, card)

    def show_qr(self, item):
        row = self.list_widget.row(item)
        booking = self.bookings[row]    
        link = hall_to_link(booking["hall"])
        if not link:
            QMessageBox.information(self, "Информация",
                                     "Для этого зала ссылка не задана.")
            return

        dlg = QDialog(self)
        dlg.setWindowTitle(f"QR‑код – {booking['hall']}")
        v = QVBoxLayout(dlg)

        qr_lbl = QLabel()
        qr_lbl.setPixmap(make_qr_pixmap(link))
        qr_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(qr_lbl)

        text = QLabel(f"Сканируйте, чтобы открыть {booking['hall']} в 2ГИС")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(text)

        dlg.exec()
          
