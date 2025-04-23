from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QStackedWidget
)
from view.login_view    import LoginView
from view.register_view import RegisterView
from view.main_app      import MainApp
import sys, pathlib

# если нужно, путь уже добавлен выше — можно оставить
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

class EntryPoint(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.resize(300, 150)

        layout = QVBoxLayout()

        # Cоздаём стек
        self.stack = QStackedWidget()

        # Готовим формы
        self.login_view    = LoginView(self.launch_main)
        self.register_view = RegisterView(
            lambda: self.stack.setCurrentWidget(self.login_view)
        )

        # --- контейнер с двумя кнопками ---
        container_layout = QVBoxLayout()
        btn_login    = QPushButton("Login")
        btn_register = QPushButton("Register")
        container_layout.addWidget(btn_login)
        container_layout.addWidget(btn_register)
        container = QWidget()
        container.setLayout(container_layout)

        # --- добавляем всё в стек ---
        self.stack.addWidget(container)
        self.stack.addWidget(self.login_view)
        self.stack.addWidget(self.register_view)
        self.stack.setCurrentWidget(container)          # <-- начальный экран

        # кнопки переключают стек
        btn_login.clicked.connect(lambda: self.stack.setCurrentWidget(self.login_view))
        btn_register.clicked.connect(lambda: self.stack.setCurrentWidget(self.register_view))

        # помещаем стек в главный layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

    def launch_main(self, customer):
        self.main_app = MainApp(customer)
        self.main_app.show()
        self.close()


if __name__ == "__main__":
    print("started main")
    app = QApplication(sys.argv)
    window = EntryPoint()
    window.show()
    sys.exit(app.exec())


