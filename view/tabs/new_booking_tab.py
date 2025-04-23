from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListView, QListWidget, QMessageBox
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt6.QtCore import Qt

from controller.bookings import list_movies, list_screenings, book_ticket


THUMB_W, THUMB_H = 80, 120   # размер миниатюры


class NewBookingTab(QWidget):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        self.selected_movie = None

        main = QVBoxLayout(self)

        # --- список фильмов с постерами ---
        self.movie_view = QListView()
        self.movie_model = QStandardItemModel(self.movie_view)
        self.movie_view.setModel(self.movie_model)
        self.movie_view.clicked.connect(self.on_movie_clicked)
        main.addWidget(self.movie_view)

        # --- список сеансов выбранного фильма ---
        self.screening_list = QListWidget()
        self.screening_list.itemClicked.connect(self.book_selected_screening)
        main.addWidget(self.screening_list)

        self.load_movies()

    # ------------------------------------------------------------------ #
    # загрузка фильмов в модель с постерами
    def load_movies(self):
        self.movies = list_movies()
        self.movie_model.clear()

        for movie in self.movies:
            item = QStandardItem(f"{movie.title}  |  rating: {movie.rating}  |  description: {movie.description}  |  genre: {movie.genre}")
            # создать миниатюру постера
            try:
                pixmap = QPixmap(movie.picture) \
                    .scaled(THUMB_W, THUMB_H, Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation)
                item.setIcon(QIcon(pixmap))
            except Exception:
                pass   # если картинка не загрузилась – просто текст
            # отключаем редактирование
            item.setEditable(False)
            self.movie_model.appendRow(item)

    # ------------------------------------------------------------------ #
    # при клике на фильм загружаем список сеансов
    def on_movie_clicked(self, index):
        self.selected_movie = self.movies[index.row()]
        self.load_screenings()

    def load_screenings(self):
        screenings = list_screenings(self.selected_movie.id)
        self.screening_list.clear()

        for s in screenings:
            self.screening_list.addItem(
                f"{s.datetime}  |  {s.hall}  |  Осталось мест: {s.seats_left}"
            )

    # ------------------------------------------------------------------ #
    # бронируем выбранный сеанс
    def book_selected_screening(self, item):
        index = self.screening_list.row(item)
        screening = list_screenings(self.selected_movie.id)[index]

        ok = book_ticket(self.customer.id, screening.id, 1)  
        if ok:
            QMessageBox.information(self, "Успех", "Билет забронирован!")
            self.load_screenings()         
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось забронировать.")
