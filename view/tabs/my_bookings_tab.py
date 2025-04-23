from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget,
    QPushButton, QListWidgetItem, QLabel
)
from PyQt6.QtGui  import QPixmap
from PyQt6.QtCore import Qt

from controller.bookings import get_my_bookings   # «обогащённые» данные


class MyBookingsTab(QWidget):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer

        self.layout = QVBoxLayout(self)

        # ── кнопка обновления ────────────────────────────────
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.reload_data)
        self.layout.addWidget(refresh_btn)

        # ── список бронирований ─────────────────────────────
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.reload_data()          # первичная загрузка

    # --------------------------------------------------------
    def reload_data(self):
        """Очистить и заново загрузить список бронирований"""
        self.list_widget.clear()

        bookings = get_my_bookings(self.customer.id)
        for b in bookings:
            # контейнер‑карточка
            card = QWidget()
            vbox = QVBoxLayout(card)
            vbox.setContentsMargins(0, 0, 0, 0)

            # постер
            pix = QPixmap(b["picture"])
            poster_lbl = QLabel()
            poster_lbl.setPixmap(pix.scaledToWidth(120))
            vbox.addWidget(poster_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)

            # подпись
            caption = QLabel(
                f"{b['movie_title']}\n"
                f"Hall: {b['hall']}\n"
                f"{b['datetime']}"
            )
            caption.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            vbox.addWidget(caption)

            # вставляем в QListWidget
            item = QListWidgetItem()
            item.setSizeHint(card.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, card)
