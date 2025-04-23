from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from controller.account import login

class LoginView(QWidget):
    def __init__(self, on_login_success):
        super().__init__()
        self.setWindowTitle("Login")

        self.on_login_success = on_login_success

        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.attempt_login)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def attempt_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        user = login(email, password)
        if user:
            self.on_login_success(user)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid email or password.")
