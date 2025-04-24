from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QStackedWidget
)
from view.login_view import LoginView
from view.register_view import RegisterView
from view.main_app import MainApp
import sys, pathlib


sys.path.append(str(pathlib.Path(__file__).resolve().parent))

class EntryPoint(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.resize(300, 150)

        layout = QVBoxLayout()

        
        self.stack = QStackedWidget()

    
        self.login_view    = LoginView(self.launch_main)
        self.register_view = RegisterView(
            lambda: self.stack.setCurrentWidget(self.login_view)
        )

    
        container_layout = QVBoxLayout()
        btn_login    = QPushButton("Login")
        btn_register = QPushButton("Register")
        container_layout.addWidget(btn_login)
        container_layout.addWidget(btn_register)
        container = QWidget()
        container.setLayout(container_layout)

  
        self.stack.addWidget(container)
        self.stack.addWidget(self.login_view)
        self.stack.addWidget(self.register_view)
        self.stack.setCurrentWidget(container)          

    
        btn_login.clicked.connect(lambda: self.stack.setCurrentWidget(self.login_view))
        btn_register.clicked.connect(lambda: self.stack.setCurrentWidget(self.register_view))

   
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


# from model.dao import ScreeningDAO

# sd = ScreeningDAO()
# sd.create_screening(2,"24 apr", "cosmo", 2, 0)
